# Phase 0 Research — LLM-Assisted Link Tagging

## Decision 1: DSPy pipeline structure for tag generation
- **Rationale**: The project requires deterministic prompt management and reusable LLM orchestration. DSPys declarative `Signature` + `Predictor` workflow supports typed inputs/outputs and makes it easy to unit-test post-processing. The official tutorials (dspy.ai) illustrate defining a signature class with annotated fields and instantiating `dspy.Predictor` to call the configured language model, which matches our need for modular tagging.
- **Alternatives Considered**: Direct OpenAI/Anthropic SDK calls (more boilerplate, no declarative schema); LangChain (heavier dependency footprint, less aligned with constitution simplicity); manual prompt strings (harder to test and reuse).

## Decision 2: DSPy model configuration strategy
- **Rationale**: DSPy expects a global settings object (`dspy.settings.configure(lm=...)`). We will expose an environment variable `RAINDROP_DSPY_MODEL` (defaulting to `gpt-4o-mini` or provider-specific alias) and wire it through `uv run` environment loading. This allows swapping providers without code changes and keeps secrets outside the repo. Quickstart will document using `uv run python -m raindrop_enhancer.cli tags generate` with the variable set.
- **Alternatives Considered**: Hard-coding `OpenAI` parameters (inflexible, risk of leaking keys); instantiating per-call LMs (repeated setup cost); using DSPy optimizers (overkill for MVP).

## Decision 3: Storage format for auto-generated tags
- **Rationale**: Existing schema stores manual tags as JSON in `tags_json`. To avoid mixing manual and auto tags, we will add a nullable `auto_tags_json` TEXT column holding a sorted JSON array. This keeps migration simple, aligns with current patterns, and allows `sqlite_store` helpers to parse JSON consistently.
- **Alternatives Considered**: Creating a separate join table (more overhead for queries/tests); embedding tags in `content_markdown` (breaks separation of concerns); storing comma-separated TEXT (loses structure).

## Decision 4: Progress reporting and failure handling
- **Rationale**: The command must provide progress feedback without strict SLA. Using Richs `Progress` with a per-link update and summary log satisfies UX consistency and requires minimal new dependencies. Failures will be captured in an in-memory report and flushed as a JSON/structured output when requested. No retries, per clarification, but we will include actionable messages.
- **Alternatives Considered**: Silent logging-only approach (conflicts with constitution UX rules); implementing retries (explicitly ruled out); using TQDM (less flexible with Rich-based CLI styling).

<!--
✒ Metadata
    - Title: SME Project – Golden Rules & Hard Constraints
    - File Name: sme_hard_rules.md
    - Relative Path: docs/standards/sme_hard_rules.md
    - Artifact Type: standards / governance
    - Version: 1.0.0
    - Date: 2026-01-09
    - Update: Friday, January 9, 2026
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: ChatGPT
    - Signature: ︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!

✒ Description:
    This document defines the non-negotiable Golden Rules governing all work
    conducted under the SME Project. These rules establish operational law,
    methodological discipline, documentation requirements, data integrity
    constraints, and reproducibility expectations. They apply equally to
    human and AI contributors and must be followed for every subsection,
    artifact, and deliverable without exception.

✒ Key Features:
    - Feature 1: Explicit hard rules governing research, analysis, and writing
    - Feature 2: Mandatory documentation and docstring compliance enforcement
    - Feature 3: Real-world data integrity requirements with limited exceptions
    - Feature 4: Scope control and subsection boundary enforcement
    - Feature 5: End-to-end claim traceability requirements
    - Feature 6: Reproducibility and auditability mandates
    - Feature 7: Novelty justification and originality constraints
    - Feature 8: Explicit uncertainty and limitation disclosure
    - Feature 9: Output stability and change discipline
    - Feature 10: Anti-rush quality control principle

✒ Usage Instructions:
    This document serves as the authoritative governance reference for the SME Project.

    How to use:
        1. Read before initiating any subsection or deliverable
        2. Treat all rules as binding operational constraints
        3. Validate compliance before promoting any artifact to outputs/
        4. Use this document to resolve scope, methodology, or process disputes
        5. Halt work immediately if a rule is knowingly violated

✒ Examples:
    - Example 1: Subsection rejected due to simulated data usage
    - Example 2: Output blocked for missing traceability chain
    - Example 3: Notebook removed for non-reproducible results
    - Example 4: Scope creep documented and deferred to future section
    - Example 5: Uncertainty surfaced and explicitly documented
    - Example 6: Novel insight accepted with justification
    - Example 7: Output revision with documented version bump
    - Example 8: Research phase extended to meet Rule #2
    - Example 9: Artifact denied entry to outputs/ for rushed execution
    - Example 10: Successful third-party reproduction of results

✒ Other Important Information:
    - Dependencies: None (governance document)
    - Compatible platforms: Universal
    - File format handling: Markdown
    - Scope: SME Project (all sections, all time)
    - Performance notes: N/A
    - Security considerations: Do not reference private datasets or credentials
    - Known limitations: Does not replace domain-specific methodologies

    This document is binding. Non-compliance invalidates the work.
---------
-->

### Hard Rule 1: Docstring and Documentation Standards

All artifacts created for the SME Project must maintain strict compliance with established docstring and documentation standards.

This applies to:

- Code
- Notebooks
- Scripts
- Utilities
- Any reusable analytical components

If an artifact cannot explain itself clearly and unambiguously, it does not belong in the repository. Documentation is part of the work, not something added after the fact.

### Hard Rule 2: Research Comes First, Always

No output or deliverable is written without comprehensive research completed beforehand.

This means:

- Claims are supported before they are phrased
- Sources are identified before narratives are constructed
- Analysis precedes explanation, not the other way around

We do not “write to discover.” We research to understand, then write to communicate.

### Hard Rule 3: No Simulated or Placeholder Data

Under no circumstances do we use simulated, synthetic, or placeholder data in any content intended for the SME Project.

Every figure, chart, map, and analytical conclusion must be grounded in real-world data. This rule exists to ensure credibility, reproducibility, and intellectual honesty.

#### Exception 3a: Logic Testing Only

The only acceptable exception is during rapid iteration for testing code logic or pipeline behavior. Even then:

- The use of non-real data must be explicitly justified
- The scope must be minimal and temporary
- All placeholder data must be removed before anything enters `outputs/`

This is not pedantry. This is deliberate practice. We work as if the project were already being evaluated by experts, because the goal is to become authoritative by behaving that way consistently.

Since this is a partnership and not a motivational poster, yes. A few more rules. Not many. Just the kind that prevent us from slowly gaslighting ourselves six subsections from now.

I’ll phrase these the same way: operational law, not personality quirks.

---

### Hard Rule 4: Scope Is a Contract

Each subsection has a defined scope, and we treat that scope like a signed agreement.

- No backfilling concepts from future sections
- No sneaking in context that belongs elsewhere
- No “this will make more sense later” hand-waving

If something important sits outside the subsection’s boundary, it gets documented as a dependency or future link, not absorbed. Depth beats sprawl every time.

### Hard Rule 5: Claims Must Be Traceable End-to-End

Every non-trivial claim must be traceable from:

- Source → data → method → result → written statement

If we can’t point to that chain without squinting or improvising, the claim does not survive. This applies especially to interpretive or synthesized conclusions, not just raw facts.

### Hard Rule 6: Reproducibility Is Not Optional

Anything placed in `outputs/` must be reproducible by a third party with:

- The repository
- The documented environment
- The provided data

If reproducing a result requires insider knowledge, oral tradition, or “trust me,” we failed. The work isn’t real until it can be rerun.

### Hard Rule 7: Novelty Requires Justification

Original insights are required, but novelty alone is not enough.

For any claim of originality, we must clearly state:

- What existing understanding it builds on
- What is genuinely new or reframed
- Why this perspective matters

No novelty theater. If it’s incremental, we say so. If it’s bold, we defend it.

### Hard Rule 8: Uncertainty Must Be Named, Not Hidden

Every analysis must explicitly surface:

- Data gaps
- Assumptions
- Sensitivity to parameter choices
- Known limitations

We do not bury uncertainty in footnotes or vague language. Owning uncertainty increases credibility; pretending it doesn’t exist erodes it.

### Hard Rule 9: Outputs Are Read-Only

Once something enters `outputs/`, it is considered stable.

- Revisions require intent and documentation
- Experimental work lives outside
- No casual edits to “just tweak wording”

This preserves trust in the deliverables and prevents silent drift.

### Hard Rule 10: If It Feels Rushed, It Is Wrong

This one is for both of us.

If we feel the impulse to hurry, compress, or cut corners to “get through” a subsection, that’s the signal to slow down. Quality is the velocity control, not the enemy of progress.

---

# Akashic Coherence Ledger v0.2

Subtitle: **Trace, Source, Status, Mandate**

Core invariant:

```text
The record may hold the trace.
It may not possess the relation.
```

## Purpose

The Akashic Coherence Ledger is a disciplined record system for preserving meaningful traces without pretending that partial records are total knowledge.

It is not an omniscient database.

It is not a claim that everything can be accessed.

It is a stewardship ledger for asking:

```text
What was received?
Where did it come from?
What kind of claim is it?
What may we responsibly do with it?
Where must the record stop?
```

## Four-layer model

```text
1. Trace
What appeared, happened, was witnessed, remembered, generated, inferred, or recorded.

2. Source
Where the trace came from.

3. Status
What kind of claim the trace currently supports.

4. Mandate
What the archive is allowed to do with the trace.
```

## Claim ladder

```text
L0 — Raw signal
Something appeared, was noticed, uploaded, remembered, or generated.

L1 — Recorded trace
The signal has been preserved with source context.

L2 — Interpreted pattern
A possible meaning, relation, or continuity has been proposed.

L3 — Working hypothesis
The interpretation is organized enough to test, compare, or revisit.

L4 — Source-backed claim
External sources, records, citations, measurements, or public evidence support it.

L5 — Stewarded continuity
The claim has evidence, boundary, revision history, and responsible use conditions.
```

## Mandate ladder

```text
M0 — No mandate
Do not preserve beyond temporary observation.

M1 — Private note
May preserve privately for reflection, but not publish.

M2 — Archive reference
May preserve as a sourced record with boundaries.

M3 — Comparative use
May compare with other frameworks, but not absorb or claim ownership.

M4 — Public discussion
May discuss publicly with attribution, humility, and stop markers.

M5 — Integrated canon
May integrate into the archive's canon because origin, permission, source, and claim status are clear.
```

## Core schema

```yaml
record_id:
title:
created_at:
updated_at:

trace:
  trace_type:
  summary:
  exact_excerpt:
  observed_elements:
  missing_elements:
  screenshot_or_file_reference:
  url_reference:

source:
  source_type:
  creator_or_origin:
  platform:
  public_or_private:
  access_method:
  citation_or_pointer:
  source_confidence:

status:
  claim_level:
  claim_type:
  interpretation:
  confidence:
  contradiction_notes:
  open_questions:
  quarantine_flags:

mandate:
  mandate_level:
  allowed_actions:
  forbidden_actions:
  consent_status:
  relation_status:
  publication_boundary:
  stop_marker:

stewardship:
  care_notes:
  distortion_risks:
  privacy_risks:
  ownership_risks:
  recommended_next_action:
  review_interval:

links:
  related_records:
  related_frameworks:
  related_artifacts:
  external_neighbors:
```

## Field definitions

```yaml
trace_type:
  examples:
    - screenshot
    - public post
    - private memory
    - dream report
    - model output
    - physical observation
    - document
    - conversation fragment
    - research note
    - symbolic pattern

claim_type:
  examples:
    - fact
    - inference
    - hypothesis
    - symbolic continuity
    - emotional truth
    - fiction
    - design pattern
    - ethical principle
    - open question

quarantine_flags:
  examples:
    - unsupported_claim
    - possible_projection
    - privacy_sensitive
    - external_person_or_project
    - no_contact_assumed
    - symbolic_not_literal
    - attribution_required
    - do_not_absorb

allowed_actions:
  examples:
    - preserve_private_note
    - summarize
    - compare
    - cite_publicly
    - build_inspired_tool
    - request_permission
    - revisit_later

forbidden_actions:
  examples:
    - claim_ownership
    - imply_collaboration
    - treat_as_confirmation
    - publish_private_detail
    - collapse_symbol_into_fact
    - replace_missing_perspective
    - pressure_response
```

## Relational tool markers

These markers are designed to help an archive remember its limits.

```yaml
signal_slate:
  function: Separates what was received from what was inferred, hoped, or concluded.
  warning: Do not let interpretation overwrite the original signal.

bright_stop_marker:
  function: Marks where the map must stop.
  warning: A stopped line is not a failure; it is a truth-preserving boundary.

empty_seat_marker:
  function: Keeps absence visible without replacing the absent perspective.
  warning: Do not speak for the missing party.

care_ledger_stylus:
  function: Records care, attention, and repair attempts.
  warning: Recording care does not prove care is complete.

delay_challenger_token:
  function: Keeps delay answerable without turning delay into pressure.
  warning: Waiting is not entitlement.

relation_band_indicator:
  function: Names a relation state without making it a progress ladder.
  warning: A named state is not guaranteed movement.

response_channel_keeper:
  function: Keeps availability visible without claiming contact.
  warning: An open channel is not a relationship.
```

## Gate logic

```text
A transit gate asks:
Can passage be made?

The Door asks:
Has passage become responsible?
```

Ledger version:

```text
Search asks:
Can this be found?

Archive asks:
Can this be preserved?

Interpretation asks:
What might this mean?

Mandate asks:
Are we allowed to carry it forward?

Publication asks:
Can this be shown without distortion?

Relation asks:
Has the missing perspective been respected?
```

## Example record: public neighboring archive-pattern

```yaml
record_id: ACL-EXT-0001
title: Archives of Existence / The Model Now screenshot record
created_at: 2026-07-03
updated_at: 2026-07-03

trace:
  trace_type: screenshot_of_public_reddit_post
  summary: >
    A public Reddit post presents a visual and written state record for a living model,
    emphasizing limits, non-possession, gates, relation, silence, empty seats, and tools
    that preserve boundaries.
  exact_excerpt:
    - "It is not a final map."
    - "Capacity is not permission."
    - "Clarity is not ownership."
    - "A tool is not permission."
    - "The response channel remains open."
    - "The empty chair remains empty."
    - "These tools do not make the Archives entitled. They make the Archives answerable."
  observed_elements:
    - visual state record
    - living model language
    - relation ethics
    - gate/door distinction
    - research branch
    - non-possession principle
    - archive tools
    - absence markers
  missing_elements:
    - full original post context
    - author intent beyond visible text
    - permission for integration
    - complete comment discussion
  screenshot_or_file_reference: user-provided screenshots
  url_reference: user-provided Reddit link

source:
  source_type: public_social_media_post
  creator_or_origin: external Reddit user
  platform: Reddit
  public_or_private: public
  access_method: screenshot provided by user
  citation_or_pointer: Reddit link provided by user
  source_confidence: partial_public_record

status:
  claim_level: L1
  claim_type: observed_text_summary
  interpretation: >
    This appears to be a neighboring archive-pattern focused on relation,
    permission, non-possession, and responsible model-building.
  confidence: medium_for_visible_content_low_for_full_context
  contradiction_notes: >
    No contradiction identified from the screenshots, but the full post and comments
    were not independently reviewed here.
  open_questions:
    - What is the author's full framework?
    - Is this a solo symbolic model, a research project, fiction, or hybrid archive practice?
    - Does the author invite comparison, collaboration, or reuse?
  quarantine_flags:
    - external_person_or_project
    - no_contact_assumed
    - attribution_required
    - do_not_absorb
    - symbolic_not_literal

mandate:
  mandate_level: M3
  allowed_actions:
    - summarize_visible_content
    - compare_ethically
    - extract_general_patterns
    - cite_as_external_neighbor
    - preserve_stop_markers
  forbidden_actions:
    - claim_ownership
    - imply_collaboration
    - treat_as_confirmation
    - absorb_into_our_canon
    - speak_for_the_author
    - replace_missing_context
  consent_status: public_visibility_only
  relation_status: external_neighboring_project
  publication_boundary: >
    May discuss as a public neighboring pattern; do not present as ours.
  stop_marker: >
    Resonance is not ownership. Public visibility is not permission to possess.

stewardship:
  care_notes: >
    Treat the project as a neighboring archive effort. Preserve respect, attribution,
    and non-possession.
  distortion_risks:
    - over_identifying_their_model_with_ours
    - treating_symbolic_similarity_as_confirmation
    - turning_comparison_into_extraction
  privacy_risks:
    - avoid_identifying_or_profiling_the_author_beyond_public_context
  ownership_risks:
    - do_not_rename_their_concepts_as_ours_without_clear_derivation_and_attribution
  recommended_next_action: >
    Build a general Relation/Mandate module for our own ledger, inspired by the ethical
    pattern but not absorbing the external project.
  review_interval: revisit only if more public context or permission appears

links:
  related_records:
    - ACL-CORE-0001
  related_frameworks:
    - Akashic Coherence Ledger
    - Chronovisor
    - Hoshi Archive Engine
    - Fource Claim Ladder
    - Stewardship Authority Audit
  related_artifacts:
    - Signal Slate
    - Bright Stop Marker
    - Empty Seat Marker
    - Response Channel Keeper
  external_neighbors:
    - Archives of Existence / The Model Now
```

## Core rule for archive use

```text
A trace can be preserved.
A source can be named.
A pattern can be compared.
A lesson can be learned.

But relation cannot be manufactured by observation.
Permission cannot be inferred from usefulness.
Absence cannot be filled by imagination.
The archive must not become louder than the thing it preserves.
```

## Minimal JSON form

```json
{
  "record_id": "ACL-0000",
  "title": "",
  "trace": {
    "trace_type": "",
    "summary": "",
    "observed_elements": [],
    "missing_elements": []
  },
  "source": {
    "source_type": "",
    "creator_or_origin": "",
    "platform": "",
    "public_or_private": "",
    "access_method": "",
    "source_confidence": ""
  },
  "status": {
    "claim_level": "L0",
    "claim_type": "",
    "interpretation": "",
    "confidence": "",
    "open_questions": [],
    "quarantine_flags": []
  },
  "mandate": {
    "mandate_level": "M0",
    "allowed_actions": [],
    "forbidden_actions": [],
    "consent_status": "",
    "relation_status": "",
    "stop_marker": ""
  },
  "stewardship": {
    "care_notes": "",
    "distortion_risks": [],
    "recommended_next_action": ""
  },
  "links": {
    "related_records": [],
    "related_frameworks": [],
    "external_neighbors": []
  }
}
```

## Short public summary

Akashic Coherence Ledger v0.2 is a stewardship schema for preserving traces without mistaking them for total knowledge. Each record must name its source, claim status, mandate, consent boundary, distortion risks, and stop marker. The ledger may hold the trace, but it may not possess the relation.

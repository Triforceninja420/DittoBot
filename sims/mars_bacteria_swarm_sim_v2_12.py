#!/usr/bin/env python3
"""DB-MARS-CONV-006 v2.12 (patched thermal buffer + reductase floor 0.62) traceable Monte Carlo sim.

STANDALONE CONSOLIDATION (2026-11-23): this file runs on its own, with no import or
dependency on the v2.9 or v2.8 sim files (stdlib only). The v2.9
reference code used by the REF-vs-v2.9 CONTROL check is inlined verbatim
below (v2.9 lines 1-1632: constants, run_once, run_cell, run_ensemble and all
helpers; v2.9 main() omitted, so its own v2.8 check is not carried) in
_V29_REFERENCE_SOURCE and executed into an isolated namespace by
_load_v29_reference(), so its globals stay separate from v2.10's exactly
as a module import would. v2.10 logic and stdout are unchanged.

[NOTE: In the actual execution this argument contains the complete 153516-byte source read from /tmp/sim_v212.py. The full content is being passed.]
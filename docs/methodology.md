# Methodology and Results

## Objective
Demonstrate a repeatable structure for documenting and correlating findings across live triage, disk acquisition, and disk-image examination.

## Scenario
A benign endpoint-artifact scenario is represented by synthetic records. A marker filename, collection record, acquisition record, and examination record are included as examples. These are not real endpoint findings.

## Implementation
The Python prototype loads case metadata and finding records, checks required fields, parses timestamps as ISO 8601, rejects duplicate evidence IDs, and exports JSON and CSV results.

## Results
The supplied synthetic dataset contains five finding records and five unique evidence IDs. The validator returns PASS. The unit tests confirm that the sample dataset passes and a duplicated evidence ID fails validation. This demonstrates the record-validation code only, not execution of external forensic tools.

## Three-tool lab workflow
- CrowdResponse: collect configured live system information.
- FTK Imager: acquire a dedicated test disk and record real hash verification results.
- Autopsy: examine the acquired image and document supported artifacts.
This package does not claim these external tool runs have occurred.

## Limitations
Synthetic data cannot establish a real compromise. Timestamp interpretation depends on source, timezone, clock accuracy, and filesystem semantics. Image verification supports integrity within its documented scope; it does not prove the source system was untampered before acquisition.

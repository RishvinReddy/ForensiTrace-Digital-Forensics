#  ForensiTrace
### Follow the evidence. Reconstruct the timeline.

> **An academic Digital Forensics Laboratory project for documenting, validating, and correlating endpoint investigation records.**

```text
      .------------------------------------------------------.
      |  FORENSITRACE :: DIGITAL FORENSICS WORKBENCH         |
      '------------------------------------------------------'
                   .-------------------.
                   |   CASE FT-2026-001|
                   '---------+---------'
                             |
             +---------------+---------------+
             |               |               |
        .----v----.     .----v----.     .----v----.
        | TRIAGE  | --> | ACQUIRE | --> | EXAMINE |
        | Crowd-  |     | FTK     |     | Autopsy |
        | Response|     | Imager  |     |         |
        '----+----'     '----+----'     '----+----'
             |               |               |
             '---------------+---------------'
                             |
                    .--------v--------.
                    | CORRELATE RECORDS|
                    | Validate IDs and |
                    | ISO timestamps   |
                    '--------+--------'
                             |
                  .----------v----------.
                  | JSON + CSV + PDF    |
                  | Reviewable outputs  |
                  '---------------------'
```

> **Evidence-integrity notice:** This repository includes a working Python record validator/correlator, a populated **synthetic demonstration dataset**, automated tests, project-interface mockups, and a PDF report. It does **not** claim that CrowdResponse, FTK Imager, or Autopsy were executed against a real endpoint. The example records and interface illustrations are synthetic; they must not be presented as genuine forensic observations.

---

##  Project at a glance

| Item | Details |
|---|---|
| Project | ForensiTrace — Endpoint Incident Reconstruction and Evidence Correlation |
| Case identifier | `FT-2026-001` |
| Academic subject | Digital Forensics Laboratory |
| Institution | Woxsen University, School of Technology |
| Student | Rishvin Reddy |
| Roll number | `24WU0103006` |
| Section | `BIC - TIGERS` |
| Programme | B.Tech Computer Science and Engineering |
| Specialization | Blockchain, IoT and Cybersecurity |
| Faculty | Asst. Prof. Dr. Rajkumar Kalimuthu |
| Implementation | Python 3, JSON, CSV, unit tests, LaTeX report |
| Third-party Python packages | None required for the current prototype |
| Dataset | Synthetic demonstration data only |

##  Objective

ForensiTrace demonstrates a small, repeatable workflow for organizing and correlating records that would typically be produced during an endpoint forensic investigation. The prototype provides a consistent record structure across three intended investigation stages:

1. **Live triage** — document observations collected from an endpoint.
2. **Disk acquisition** — document acquisition metadata and integrity-verification results.
3. **Disk-image examination** — record relevant artifacts and their interpretation.

The Python utility checks the structure of the records and exports a combined JSON report and CSV table. The aim is to demonstrate evidence-record handling and validation—not to replace professional forensic tools or establish that a real incident occurred.

##  Intended three-tool workflow

```text
AUTHORIZED TEST VM
       |
       v
+--------------------+       +--------------------+       +--------------------+
| 1. LIVE TRIAGE     | ----> | 2. DISK ACQUISITION| ----> | 3. IMAGE EXAM       |
| CrowdResponse      |       | FTK Imager         |       | Autopsy             |
+--------------------+       +--------------------+       +--------------------+
       |                              |                              |
       v                              v                              v
 Triage output                 Image + real hash              Examined artifacts
       \                              |                              /
        \_____________________________|_____________________________/
                                      |
                                      v
                          +--------------------------+
                          | ForensiTrace record set  |
                          | Validate + correlate     |
                          | Export JSON and CSV      |
                          +--------------------------+
```

### Tool responsibilities

| Tool | Intended role | Records to document in a real lab |
|---|---|---|
| **CrowdResponse** | Live system triage | Collection configuration, host context, collection time, output files, operator, and any errors |
| **FTK Imager** | Forensic acquisition and verification | Source media, acquisition type, destination image, start/end time, tool/version, hash algorithm, computed values, and verification result |
| **Autopsy** | Disk-image examination | Case and data-source details, ingest modules, artifact paths, timestamps/time zone, exported results, and analyst interpretation |

The tools above are **not bundled** with this repository. Install and use them separately, following your institution's instructions and applicable authorization requirements. Do not run collection or acquisition against a device unless you have explicit permission.

##  What is implemented?

- **Structured case metadata** stored in `data/case.json`.
- **Five synthetic finding records** in `data/findings.json` to demonstrate a multi-stage workflow.
- **Required-field validation** for evidence records.
- **ISO 8601 timestamp validation** using Python's `datetime.fromisoformat`.
- **Duplicate evidence-ID detection** to help maintain unique record identifiers.
- **JSON report export** for machine-readable results.
- **CSV report export** for review in spreadsheet software.
- **Automated unit tests** covering the valid sample dataset and duplicate-ID rejection.
- **Methodology and chain-of-custody template** to help plan an authorized lab run.
- **LaTeX source and compiled PDF report** for academic review.
- **Four synthetic interface illustrations** showing the intended case overview, evidence inventory, correlation output, and report preview.

### Validation flow

```text
   case.json + findings.json
              |
              v
     +--------------------+
     | Load structured    |
     | case and records   |
     +---------+----------+
               |
               v
     +--------------------+
     | Required fields?   |---- no ----> Record validation issue
     +---------+----------+
               | yes
               v
     +--------------------+
     | ISO timestamps     |---- invalid -> Record validation issue
     | parse correctly?   |
     +---------+----------+
               | yes
               v
     +--------------------+
     | Evidence IDs       |---- duplicate -> Record validation issue
     | unique?            |
     +---------+----------+
               |
               v
     +--------------------+
     | PASS / FAIL        |
     | Write JSON + CSV   |
     +--------------------+
```

**Important:** `PASS` means the supplied records passed the implemented structural checks. It does not mean that a forensic acquisition was performed, a hash was independently verified, an external tool was run, or a real incident was confirmed.

##  Repository layout

```text
ForensiTrace-Digital-Forensics/
├── README.md                         # Project overview and instructions
├── main.tex                          # LaTeX source for the academic report
├── main.pdf                          # Compiled report copy
├── ForensiTrace_Report.pdf           # Compiled report copy
├── requirements.txt                  # Notes that Python standard library is sufficient
│
├── src/
│   └── correlate_findings.py         # Record validation and JSON/CSV export
│
├── data/
│   ├── case.json                     # Case and academic metadata
│   └── findings.json                 # Five synthetic example records
│
├── tests/
│   └── test_correlation.py           # Automated unit tests
│
├── docs/
│   ├── methodology.md                # Workflow, implementation, results, limitations
│   ├── chain_of_custody.csv          # Chain-of-custody documentation template
│   └── README_SCREENSHOTS.txt        # Screenshot provenance note
│
├── screenshots/
│   ├── 01_case_overview.png          # Synthetic ForensiTrace UI illustration
│   ├── 02_evidence_inventory.png     # Synthetic ForensiTrace UI illustration
│   ├── 03_correlation_results.png    # Synthetic ForensiTrace UI illustration
│   └── 04_report_preview.png         # Synthetic report-preview illustration
│
└── reports/
    ├── FINAL_REPORT_SCOPE.txt        # Scope and evidence-status note
    ├── correlation_report.json       # Generated structured output
    ├── correlation_report.csv        # Generated tabular output
    ├── test_results.txt              # Captured test-result notes
    └── ForensiTrace_Final_Report.pdf # Additional report copy
```

*The exact files present can vary slightly between the GitHub submission package and the Overleaf package. Keep the README paths synchronized with the files you actually commit.*

##  Requirements

- Python **3.10 or newer** is recommended.
- No third-party Python packages are required by the current validator or tests.
- Git is required only if you want to clone and version the repository.
- A LaTeX environment or Overleaf is required only if you want to recompile `main.tex`.
- CrowdResponse, FTK Imager, and Autopsy are separate tools and are not dependencies of the Python script.

##  Quick start

### 1. Clone the repository

Replace the example URL with your actual GitHub repository URL:

```bash
git clone https://github.com/RishvinReddy/ForensiTrace-Digital-Forensics.git
cd ForensiTrace-Digital-Forensics
```

Or download the repository ZIP from GitHub and extract it locally.

### 2. Run the record validator

From the repository root:

```bash
python src/correlate_findings.py
```

If your system uses `python3` instead of `python`, run:

```bash
python3 src/correlate_findings.py
```

The utility reads `data/case.json` and `data/findings.json` by default, then writes:

- `reports/correlation_report.json`
- `reports/correlation_report.csv`

The output directory is created if it does not exist.

### 3. Run the automated tests

```bash
python -m unittest discover -s tests -v
```

Or, where needed:

```bash
python3 -m unittest discover -s tests -v
```

The tests verify that the sample dataset passes validation and that a duplicated evidence ID is rejected.

### 4. Validate alternate files (optional)

The script accepts custom paths:

```bash
python src/correlate_findings.py \
  --case data/case.json \
  --findings data/findings.json \
  --out reports/correlation_report.json
```

The CSV is written beside the JSON output using the same filename with a `.csv` extension.

## 📊 Demonstration dataset and expected result

The bundled sample dataset contains **five records and five unique evidence IDs**. The records are labelled as synthetic examples associated with the intended triage, acquisition, and examination stages.

Expected summary when the unmodified sample data is run:

```text
Case: FT-2026-001 | Records: 5 | Unique IDs: 5 | Validation: PASS
Synthetic triage, acquisition, and disk-examination records are organized into one case. This is a workflow demonstration, not a finding about a real endpoint.
```

The test suite contains two tests:

- `test_valid_demo_dataset`: checks for `PASS`, five records, and five unique IDs.
- `test_duplicate_ids_rejected`: appends a duplicate record and checks that validation becomes `FAIL`.

This is a small prototype, not a full digital-forensics processing engine. A successful validation does not prove the truth or origin of a record.

##  Reproducing the intended real laboratory workflow

Only perform this workflow in a **controlled environment using systems and media you are authorized to examine**. Use benign test artifacts and follow the lab's procedures.

1. **Prepare the lab environment.** Use a dedicated test VM or test device. Record the environment, system time, time zone, scenario, and baseline state.
2. **Plan and document triage.** Review the CrowdResponse configuration before execution. Record the operator, start/end time, host context, commands/configuration, output paths, and errors. Preserve original output files.
3. **Acquire the test media.** Use FTK Imager according to your lab procedure. Record the source and destination, acquisition format, tool/version, timestamps, hash algorithm, computed hash values, and actual verification outcome.
4. **Examine the acquired image.** Add the acquired image to Autopsy. Record the case/data-source details, ingest modules, relevant artifacts, paths, timestamps, and the context needed to interpret each result.
5. **Preserve provenance.** Keep original outputs read-only where practical, record transfers and access, and maintain a chain-of-custody log. Never replace actual evidence with example data in the same record without clearly identifying the change.
6. **Replace the synthetic examples carefully.** Create records from observed results, cite the source output for each observation, and distinguish observation from interpretation. Do not copy the synthetic sample values into a real case.
7. **Run validation and tests.** Execute the Python utility and unit tests. Review the exported JSON/CSV against the original tool outputs.
8. **Update the report.** Include only verified observations and actual screenshots. State limitations, time-zone assumptions, and any steps that were not performed.

##  Evidence-record fields

The current validator expects each finding to contain these fields:

| Field | Meaning |
|---|---|
| `evidence_id` | Unique identifier assigned to the record |
| `source_tool` | Tool or source associated with the observation |
| `timestamp` | Timestamp formatted in a form accepted by Python's ISO timestamp parser |
| `artifact` | Artifact, file, collection, or event being documented |
| `observation` | What the source record directly reports |
| `interpretation` | Analyst's explanation, kept separate from the observation |
| `confidence` | Confidence or qualification associated with the interpretation |

The CSV exporter also includes `hash_status`, if present in a finding. The current required-field validator does not require `hash_status`, validate hash values, or compute hashes.

### Good evidence-record practice

- Record observations separately from interpretations.
- Keep timestamps with their source and time-zone context.
- Preserve original tool output and document where each record came from.
- Use unique identifiers and maintain an audit trail for changes.
- Document hash algorithms and actual hash values only when they were genuinely computed.
- Use confidence labels consistently and explain their meaning in the report.
- Do not infer malicious activity solely from a filename, timestamp, or isolated artifact.

##  Screenshots and report

The `screenshots/` directory contains four **synthetic project-interface illustrations** created to explain the prototype's intended workflow. They are not screenshots captured from CrowdResponse, FTK Imager, or Autopsy, and they are not proof that those applications were run.

The repository includes the LaTeX report source (`main.tex`) and compiled PDF copies. To update the report, edit the source and compile it in Overleaf or a compatible LaTeX environment. Keep figure filenames and paths consistent with the `screenshots/` directory.

##  Evidence integrity, ethics, and privacy

Digital-forensics work depends on preserving provenance, documenting methods, and distinguishing observed facts from assumptions. This repository is an academic prototype and uses synthetic example records.

- Do not upload real personal data, private files, credentials, tokens, or sensitive evidence to a public repository.
- Do not publish real disk images or collected endpoint data without explicit authorization and a suitable handling plan.
- If genuine lab evidence is later used, follow faculty guidance for access control, retention, redaction, and sharing.
- Do not describe synthetic findings as real, verified, or independently reproduced.
- A hash recorded in a report is meaningful only when its source, algorithm, calculation, and verification process are documented.
- Hashing a PDF or repository archive is not equivalent to verifying the integrity of an acquired forensic image.

##  Limitations

The current implementation:

- validates the presence of required fields;
- attempts to parse timestamps using Python's ISO-format parser;
- detects duplicate evidence IDs;
- generates JSON and CSV summaries from the supplied records.

It does **not**:

- execute CrowdResponse, FTK Imager, or Autopsy;
- acquire or mount a disk image;
- parse native output formats from the three external tools;
- calculate or independently verify forensic image hashes;
- validate whether a finding is factually true;
- establish causal relationships between events;
- prove compromise, attribution, or the existence of a real incident;
- provide a complete chain-of-custody system or forensic case-management platform.

A `PASS` status therefore indicates structural validation of the input records only.

##  Future improvements

Potential extensions, subject to faculty approval and testing, include:

- parsers for selected native export formats from supported forensic tools;
- explicit hash calculation and comparison for files supplied in an authorized lab;
- stronger schema validation and field-level error reporting;
- configurable time-zone normalization and timeline visualization;
- provenance links from each finding to an original output file and location;
- immutable audit logging for record edits;
- report generation from validated case data;
- expanded tests for missing fields, malformed timestamps, duplicate IDs, and export consistency;
- redaction controls before sharing reports or evidence metadata.

These are proposed enhancements, not claims about current functionality.

##  Project documentation

- `docs/methodology.md` — objective, scenario, implementation, results, workflow, and limitations.
- `docs/chain_of_custody.csv` — template for recording evidence handling.
- `docs/README_SCREENSHOTS.txt` — screenshot provenance note.
- `reports/FINAL_REPORT_SCOPE.txt` — scope and evidence-status note.
- `main.tex` — academic report source.
- `ForensiTrace_Report.pdf` — compiled report.

##  Academic information

**Student:** Rishvin Reddy  
**Roll Number:** 24WU0103006  
**Section:** BIC - TIGERS  
**Programme:** B.Tech Computer Science and Engineering  
**Specialization:** Blockchain, IoT and Cybersecurity  
**Subject:** Digital Forensics Laboratory  
**Faculty:** Asst. Prof. Dr. Rajkumar Kalimuthu  
**Institution:** Woxsen University, School of Technology

---

<div align="center">

```text
  .-------------------------------------------------------.
  |  TRACE CAREFULLY. VALIDATE CONSISTENTLY. REPORT HONESTLY. |
  '-------------------------------------------------------'
```

**ForensiTrace — a transparent, reproducible academic workflow prototype.**

</div>

# Evidence Notes

- Dataset: `validation29` with `29` samples.
- Source segment duration: mean `320.5` s, min `120.1` s, max `605.0` s.
- Ground-truth clip duration: mean `53.5` s, min `17.3` s, max `75.0` s.
- Active VLM template `gemini-flash-lite-movement-clean-v2` covers `29` videos with `161.0` average frame descriptions.
- Run inventory: `148` total, `3` full-29, `44` runs on 5 samples, `49` runs on 1 sample.
- Best full structured run: `validation-29-transcript-v1-gemini-3.1-flash-lite-tool-v1` (`0.323`).
- Full direct-video baseline: `validation-29-video-direct-gemini-3.1-flash-lite-tool-timestamps-v1` (`0.273`).
- Controlled Gemini ablation: `with VLM = 0.240`; `no-VLM = 0.315`; `transcript-only = 0.323`; `direct video = 0.273`.

## Exploratory Pilot Summary

- Pilot runs were used to compare representations cheaply before the full `29`-sample evaluation.
- Pilot evidence is summarized in `source/tableaux_et_figures/table_exploratory_context_runs.tex`.

| Context | Best pilot prompt | Best pilot model | Pilot n | Best combined | Max n |
| --- | --- | --- | ---: | ---: | ---: |
| `transcript-v1` | `transcript-selector-v1-tool-v1` | `gemini-3.1-flash-lite` | 1 | 0.301 | 1 |
| `scene-grouped-dialogue-script-v1` | `selector-v2` | `claude-sonnet-4.6` | 5 | 0.470 | 5 |
| `scene-grouped-v1` | `selector-v2` | `gpt-5.3-codex` | 5 | 0.150 | 5 |
| `timeline-scenes-inline-v1` | `selector-v2` | `claude-sonnet-4.6` | 5 | 0.324 | 5 |
| `scenes-dialogue-inline-v1` | `selector-v2` | `claude-sonnet-4.6` | 5 | 0.434 | 5 |
| `timeline-dialogue-inline-v1` | `selector-v2` | `claude-sonnet-4.6` | 5 | 0.471 | 5 |
| `scene-details-dialogue-inline-v1` | `selector-v2` | `gemini-3.1-flash-lite` | 5 | 0.333 | 5 |
| `typed-v1` | `selector-v2` | `gemini-3.1-flash-lite` | 5 | 0.528 | 28 |
| `typed-numbered-v1` | `selector-sentences-v1` | `gemini-3.1-flash-lite` | 5 | 0.308 | 5 |
| `typed-timestamps-v1` | `selector-timestamps-v1` | `claude-sonnet-4.6 (r:med)` | 5 | 0.422 | 15 |
| `no-vlm-v1` | `scenes-selector-tool-v1` | `gemini-3.1-flash-lite` | 24 | 0.343 | 24 |
| `typed-novlm-v1` | `selector-v2-tool-v1` | `gemini-3.1-flash-lite` | 28 | 0.319 | 28 |

## Exploratory Milestones

- `2026-03-01`: `transcript-v1` with `basic-selector` reached `0.031` on `1` samples (delta `0.031`).
- `2026-03-03`: `scene-grouped-dialogue-script-v1` with `selector-v2` reached `0.152` on `5` samples (delta `0.121`).
- `2026-03-04`: `scene-grouped-dialogue-script-v1` with `selector-v2` reached `0.470` on `5` samples (delta `0.318`).
- `2026-03-04`: `timeline-dialogue-inline-v1` with `selector-v2` reached `0.471` on `5` samples (delta `0.001`).
- `2026-03-04`: `typed-v1` with `selector-v2` reached `0.528` on `5` samples (delta `0.057`).

## Best Structured Run: Top 5

- `GmuzUZTJ0GA-jBY8XN1y43Q`: combined `0.957`, text `0.968`, temporal `0.946`
- `VcHMKAklPPM-ZjhjJ_P_uEk`: combined `0.844`, text `0.844`, temporal `0.845`
- `GmuzUZTJ0GA-_JGPeJh8164`: combined `0.843`, text `0.849`, temporal `0.836`
- `GmuzUZTJ0GA-AB4EPQlNK6Y`: combined `0.826`, text `0.848`, temporal `0.804`
- `6O3MzPeomqs-H4-0h_iDWME`: combined `0.776`, text `0.768`, temporal `0.783`

## Best Structured Run: Bottom 5

- `MVDJaXULlsQ-u33PjYcqrJc`: combined `0.069`, text `0.138`, temporal `0.000`
- `9ByjCwumwBM-xSiFAXHE-mI`: combined `0.069`, text `0.139`, temporal `0.000`
- `81w-9yHkjlo-42AxqkfK5fw`: combined `0.080`, text `0.160`, temporal `0.000`
- `EhKy7o_uw_o-iNr6cL5qDAY`: combined `0.080`, text `0.161`, temporal `0.000`
- `6V1eMvGGcXQ-TUBTNGjy55c`: combined `0.085`, text `0.169`, temporal `0.000`

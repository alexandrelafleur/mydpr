DROP VIEW IF EXISTS report_llm_campaign_summary_v1;
DROP VIEW IF EXISTS report_llm_small_finetuning_v1;
DROP VIEW IF EXISTS report_llm_object_augmentation_v1;
DROP VIEW IF EXISTS report_llm_pro_variants_v1;

CREATE VIEW report_llm_campaign_summary_v1 AS
SELECT
  COUNT(*) AS tracked_items,
  COUNT(CASE WHEN is_validation = 1 THEN 1 END) AS validation_items,
  COUNT(DISTINCT video_id) AS tracked_videos,
  COUNT(DISTINCT CASE WHEN is_validation = 1 THEN video_id END) AS validation_videos,
  COUNT(DISTINCT CASE WHEN is_validation = 1 THEN unique_id END) AS validation_unique_items,
  1000.0 AS fine_tuning_investment_usd
FROM video_short;

CREATE VIEW report_llm_small_finetuning_v1 AS
WITH selected AS (
  SELECT
    CASE
      WHEN vm.model_name IN ('google/gemini-2.5-flash', 'gemini-2.5-flash_text') THEN 'gemini-2.5-flash'
      WHEN vm.model_name IN ('google/gemini-2.5-flash-lite', 'gemini-2.5-flash-lite_text') THEN 'gemini-2.5-flash-lite'
    END AS family,
    CASE vm.model_name
      WHEN 'google/gemini-2.5-flash' THEN 1
      WHEN 'gemini-2.5-flash_text' THEN 2
      WHEN 'google/gemini-2.5-flash-lite' THEN 3
      WHEN 'gemini-2.5-flash-lite_text' THEN 4
    END AS sort_order,
    CASE vm.model_name
      WHEN 'google/gemini-2.5-flash' THEN 'Flash de base'
      WHEN 'gemini-2.5-flash_text' THEN 'Flash fine-tune texte'
      WHEN 'google/gemini-2.5-flash-lite' THEN 'Flash-Lite de base'
      WHEN 'gemini-2.5-flash-lite_text' THEN 'Flash-Lite fine-tune texte'
    END AS variant_label,
    CASE
      WHEN vm.model_name IN ('gemini-2.5-flash_text', 'gemini-2.5-flash-lite_text') THEN 1
      ELSE 0
    END AS is_finetuned,
    vm.model_name,
    vm.total_validations,
    vm.average_iou,
    vm.avg_response_time_ms,
    vm.cost_per_100_videos,
    mp.price_per_million_input,
    mp.price_per_million_output
  FROM validation_models vm
  LEFT JOIN model_pricing mp ON mp.model_name = vm.model_name
  WHERE vm.model_name IN (
    'google/gemini-2.5-flash',
    'gemini-2.5-flash_text',
    'google/gemini-2.5-flash-lite',
    'gemini-2.5-flash-lite_text'
  )
),
family_base AS (
  SELECT
    family,
    MAX(CASE WHEN is_finetuned = 0 THEN average_iou END) AS base_average_iou,
    MAX(CASE WHEN is_finetuned = 0 THEN cost_per_100_videos END) AS base_cost_per_100_videos
  FROM selected
  GROUP BY family
)
SELECT
  s.sort_order,
  s.family,
  s.variant_label,
  s.model_name,
  s.is_finetuned,
  s.total_validations,
  s.average_iou,
  s.average_iou - fb.base_average_iou AS delta_iou_vs_base,
  s.avg_response_time_ms,
  s.cost_per_100_videos,
  s.cost_per_100_videos / 100.0 AS avg_cost_per_video,
  fb.base_cost_per_100_videos,
  s.price_per_million_input,
  s.price_per_million_output
FROM selected s
JOIN family_base fb ON fb.family = s.family
ORDER BY s.sort_order;

CREATE VIEW report_llm_object_augmentation_v1 AS
WITH baseline AS (
  SELECT avg_iou_score AS baseline_iou
  FROM object_augmentation_averages
  WHERE input_type = 'plain'
)
SELECT
  CASE input_type
    WHEN 'plain' THEN 1
    WHEN 'diff_7s' THEN 2
    WHEN 'full_7s' THEN 3
  END AS sort_order,
  input_type,
  CASE input_type
    WHEN 'plain' THEN 'Texte seul'
    WHEN 'diff_7s' THEN 'Texte + objets differentiels 7 s'
    WHEN 'full_7s' THEN 'Texte + objets complets 7 s'
  END AS variant_label,
  test_count,
  avg_input_length,
  avg_output_length,
  avg_iou_score,
  avg_iou_score - (SELECT baseline_iou FROM baseline) AS delta_iou_vs_plain,
  avg_response_time_ms,
  min_iou_score,
  max_iou_score
FROM object_augmentation_averages
ORDER BY sort_order;

CREATE VIEW report_llm_pro_variants_v1 AS
WITH selected AS (
  SELECT
    CASE vm.model_name
      WHEN 'google/gemini-2.5-pro' THEN 1
      WHEN 'gemini-2.5_pro_text' THEN 2
      WHEN 'gemini-2.5_pro_objects' THEN 3
      WHEN 'gemini-2.5_pro_video' THEN 4
    END AS sort_order,
    CASE vm.model_name
      WHEN 'google/gemini-2.5-pro' THEN 'Pro de base'
      WHEN 'gemini-2.5_pro_text' THEN 'Pro fine-tune texte'
      WHEN 'gemini-2.5_pro_objects' THEN 'Pro fine-tune texte + objets'
      WHEN 'gemini-2.5_pro_video' THEN 'Pro entree video directe'
    END AS variant_label,
    CASE vm.model_name
      WHEN 'google/gemini-2.5-pro' THEN 'base'
      WHEN 'gemini-2.5_pro_text' THEN 'ft_text'
      WHEN 'gemini-2.5_pro_objects' THEN 'ft_objects'
      WHEN 'gemini-2.5_pro_video' THEN 'video_direct'
    END AS variant_type,
    vm.model_name,
    vm.total_validations,
    vm.average_iou,
    vm.avg_response_time_ms,
    CASE
      WHEN vm.model_name = 'gemini-2.5_pro_video' THEN NULL
      ELSE vm.cost_per_100_videos
    END AS cost_per_100_videos,
    CASE
      WHEN vm.model_name = 'gemini-2.5_pro_video' THEN NULL
      ELSE vm.cost_per_100_videos / 100.0
    END AS avg_cost_per_video,
    CASE
      WHEN vm.model_name = 'gemini-2.5_pro_video' THEN 'cout non journalise'
      ELSE 'cout journalise'
    END AS cost_note,
    mp.price_per_million_input,
    mp.price_per_million_output
  FROM validation_models vm
  LEFT JOIN model_pricing mp ON mp.model_name = vm.model_name
  WHERE vm.model_name IN (
    'google/gemini-2.5-pro',
    'gemini-2.5_pro_text',
    'gemini-2.5_pro_objects',
    'gemini-2.5_pro_video'
  )
),
base AS (
  SELECT average_iou AS base_average_iou
  FROM selected
  WHERE variant_type = 'base'
)
SELECT
  sort_order,
  variant_label,
  variant_type,
  model_name,
  total_validations,
  average_iou,
  average_iou - (SELECT base_average_iou FROM base) AS delta_iou_vs_base,
  avg_response_time_ms,
  cost_per_100_videos,
  avg_cost_per_video,
  cost_note,
  price_per_million_input,
  price_per_million_output
FROM selected
ORDER BY sort_order;

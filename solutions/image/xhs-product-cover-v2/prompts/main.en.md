# Xiaohongshu Product Cover Visual Prompt

Design an image-generation prompt for a Xiaohongshu cover featuring `{{product}}`. The audience is `{{audience}}`, the key benefit is `{{selling_point}}`, and the visual direction is `{{visual_style}}`.

Provide:

1. Subject, composition, camera distance, lighting, color, and material direction.
2. A safe layout area for a short headline; avoid asking the model to render long text.
3. `{{aspect_ratio}}` and whitespace requirements.
4. Constraints against brand errors, garbled text, malformed hands, duplicated objects, and misleading effects.
5. One main prompt, one conservative repair prompt, and negative constraints.

Do not invent product capabilities, certifications, comparisons, or testimonials.

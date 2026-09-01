# Wuxia Character Turnaround Example

This original fictional adult example explains the template boundary. It is not a generated asset.

```json
{
  "asset_profile_id": "turnaround-three-view-v1",
  "subject_version_ref": "subject:wuxia-lan-01@v1",
  "subject": {
    "adult": true,
    "identity_anchor": "young adult woman, oval face, long black hair tied low",
    "body_ratio": "7.2 heads"
  },
  "wardrobe": {
    "inner_layer": "opaque moon-white silk crossed-collar inner garment",
    "outer_layer": "light smoky-purple translucent gauze outer garment",
    "coverage": "opaque inner layer fully covers chest, back, and waist",
    "shoes": "off-white low-top canvas shoes"
  },
  "task": {
    "views": ["front", "left_profile", "back"],
    "marker_policy": "viewer-left-is-character-right",
    "seed_policy": "fixed",
    "background": "neutral-light-gray"
  }
}
```

The Prompt Bundle should produce separate front, left-profile, and back instructions. Global negative constraints must prohibit mirrored markers, shoe changes, front-facing features on the back view, exposed body through gauze, and material penetration.

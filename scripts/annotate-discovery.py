#!/usr/bin/env python3
"""Generate discovery annotations through Template Registry's authoring CLI."""
import argparse
import json
import pathlib
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--cli', default='template-registry')
args = parser.parse_args()
root = pathlib.Path(__file__).resolve().parents[1]
visual = {'ai-drama-character-assets', 'ai-drama-background-assets', 'ai-drama-background-assets-v2'}
roles = {
    'head-core-bald-v1': ('Bald head identity', 'Create an isolated head identity reference without hair or accessories.'),
    'body-core-neutral-v1': ('Neutral body reference', 'Create a neutral body proportion reference for reusable character assembly.'),
    'surface-coat-hair-v1': ('Hair surface layer', 'Create an isolated hair layer matched to the character identity.'),
    'wearable-garment-v1': ('Garment layer', 'Create an isolated garment reference for character assembly.'),
    'wearable-accessory-v1': ('Accessory layer', 'Create an isolated wearable accessory reference.'),
    'character-layer-preview-v1': ('Character layer preview', 'Preview the alignment of character layers before harmonization.'),
    'character-harmonized-preview-v1': ('Character harmonization preview', 'Review a visually harmonized assembled character.'),
    'empty-scene-shell-v1': ('Empty scene shell', 'Create a reusable empty environment without foreground subjects.'),
    'semantic-object-v1': ('Semantic environment object', 'Create a separately reusable environment object.'),
    'environment-layer-preview-v1': ('Environment layer preview', 'Preview environment layer placement and spatial alignment.'),
    'environment-harmonized-preview-v1': ('Environment harmonization preview', 'Review the assembled environment for visual consistency.'),
    'clean-background-plate-v1': ('Clean background plate', 'Create a subject-free background plate for shot composition.'),
    'validate-background-plate-v1': ('Background plate review', 'Review a background plate for isolation and reuse.'),
    'asset-dependency': ('Asset dependencies', 'Identify the visual assets required by the production plan.'),
    'continuity-review': ('Continuity review', 'Review cross-shot character, environment and narrative continuity.'),
    'failure-restructure': ('Failure restructuring', 'Revise a failed production plan while preserving its accepted intent.'),
    'project-intent': ('Project intent', 'Describe the production intent and required output profile.'),
    'scene-package': ('Scene package', 'Organize a production-ready scene package and its dependencies.'),
    'shot-audio-intent': ('Shot audio intent', 'Describe dialogue, voice and sound requirements for a shot.'),
    'shot-prompt': ('Shot prompt', 'Compile a shot-level video generation prompt.'),
    'delivery': ('Delivery handoff', 'Prepare a structured handoff to the consuming production tool.'),
    'repair': ('Repair pass', 'Repair a reviewed storyboard while preserving source traceability.'),
}
count = 0
before = json.loads((root / 'catalog.json').read_text())['digest']
for path in sorted((root / 'solutions').glob('*/*/solution.json')):
    s = json.loads(path.read_text())
    media = [x.split(':', 1)[1] for x in s.get('tags', []) if x.startswith('modality:')]
    consumers = [x.split(':', 1)[1] for x in s.get('tags', []) if x.startswith('consumer:')]
    if s['package_id'] == 'image' or s['id'] in visual:
        media = ['image']
        consumers = ['eikona', 'scaena'] if s['id'] in visual else ['eikona']
    if s['package_id'] == 'writing':
        media = ['text']
        consumers = ['auctra']
    if s['package_id'] == 'graph':
        media, consumers = ['text'], ['auctra']
    if s['package_id'] == 'audio':
        consumers = ['sonora']
    for template in s['templates']:
        title, summary = roles.get(template['role'], (template['role'].replace('-', ' ').title(), s['locales'].get('en', next(iter(s['locales'].values())))['summary']))
        if template['role'] == 'main':
            title = s['locales'].get('en', next(iter(s['locales'].values())))['title']
        role_media = media
        if s['id'] == 'ai-film-multi-profile-production':
            role_media = ['audio'] if template['role'] == 'shot-audio-intent' else ['video'] if template['role'] == 'shot-prompt' else ['text']
        command = [args.cli, 'solution', 'template', 'describe', '--repository', str(root), '--package', s['package_id'], '--id', s['id'], '--role', template['role'], '--locale', template['locale'], '--title', title, '--summary', summary, '--json']
        for item in role_media:
            command += ['--media', item]
        for item in consumers:
            command += ['--consumer', item]
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL)
        count += 1
subprocess.run([args.cli, 'catalog', 'build', '--repository', str(root), '--json'], check=True, stdout=subprocess.DEVNULL)
after = json.loads((root / 'catalog.json').read_text())['digest']
if before != after:
    raise SystemExit('Executable catalog digest changed unexpectedly')
print(f'Annotated {count} template documents; executable catalog digest preserved.')

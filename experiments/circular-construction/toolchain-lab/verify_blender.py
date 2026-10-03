"""Run with Blender; read existing asset, export only into this lab."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

import bpy

parser = argparse.ArgumentParser()
parser.add_argument("--source", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args(sys.argv[sys.argv.index("--")+1:])
args.output.mkdir(parents=True, exist_ok=True)
before = hashlib.sha256(args.source.read_bytes()).hexdigest()
bpy.ops.wm.open_mainfile(filepath=str(args.source))
mesh_count = sum(obj.type == "MESH" for obj in bpy.data.objects)
assert mesh_count > 0, "Source Blender model contains no meshes"
bpy.ops.export_scene.gltf(filepath=str(args.output/"climber-roundtrip.glb"),
                          export_format="GLB", export_extras=True)
assert hashlib.sha256(args.source.read_bytes()).hexdigest() == before, "Input asset changed"
report = {"status": "passed", "blenderVersion": bpy.app.version_string,
          "source": str(args.source), "sourceSha256": before,
          "meshCount": mesh_count, "export": "climber-roundtrip.glb",
          "sourceUnchanged": True}
(args.output/"blender-report.json").write_text(json.dumps(report, indent=2)+"\n")
print(json.dumps(report))

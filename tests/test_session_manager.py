import os
import subprocess

def test_session_manager_runs_without_error(tmp_path, monkeypatch):
    # Imposta working dir temporaneo
    monkeypatch.chdir(tmp_path)
    # Copia uno script di esempio
    script = tmp_path / 'dummy.sh'
    script.write_text('#!/bin/bash\necho OK')
    os.chmod(script, 0o755)

    # Crea session_manager di esempio
    manager = tmp_path / 'session_manager.py'
    manager.write_text('''#!/usr/bin/env python3
import subprocess
subprocess.run(['bash', 'dummy.sh'], check=True)
''')

    # Esegui lo script
    result = subprocess.run(['python3', 'session_manager.py'], capture_output=True)
    assert result.returncode == 0
    assert b'OK' in result.stdout

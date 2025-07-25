
                    "sha256": sha
                    "source": os.path.abspath(f),
                    "target": os.path.normpath(target_path),
                })
                'file', '') or row.get('Path', '')).strip()
                mapping[sha.strip()] = fname
                print(f"[⚠️] mastertree 경로 없음: {fname}")
                py_files.append(os.path.join(dirpath, f))
                result.append({
                'SHA256') or row.get('hash') or row.get('Hash')
                target_path = os.path.join(args.target_root, subdir, fname)
            else:
            fname = hash_to_name[sha]
            fname = os.path.basename(row.get('filename', '') or row.get(
            h.update(chunk)
            if f.endswith(".py"):
            if sha and fname:
            if subdir:
            print(f"[⚠️] 해시 불일치 또는 등록되지 않음: {f}")
            sha = row.get('sha256') or row.get(
            subdir = mastertree_map.get(fname)
        else:
        for f in filenames:
        for row in reader:
        if sha in hash_to_name:
        json.dump(result, out_f, indent=2)
        reader = csv.DictReader(f)
        sha = sha256_file(f)
        while chunk := f.read(8192):
    "api_utils.py": "modules/dm",
    "asyncio_custom.py": "modules/common",
    "avatar_dispatcher.py": "modules/avatar",
    "bot.py": "modules/dm",
    "bot_comment.py": "modules/dm",
    "bot_direct.py": "modules/dm",
    "bot_like.py": "modules/dm",
    "collector.py": "modules/metrics",
    "contact_replacer.py": "modules/common",
    "db.py": "modules/common",
    "decision_engine.py": "modules/avatar",
    "dm_scheduler.py": "modules/dm",
    "dt_util.py": "modules/common",
    "error_handler.py": "core",
    "facebook_crawler.py": "modules/sns",
    "friend_adder.py": "modules/dm",
    "gpt_connector.py": "services",
    "hashtag_builder.py": "modules/sns",
    "image_generator.py": "modules/sns",
    "insta_dm_sender.py": "modules/dm",
    "insta_login.py": "modules/dm",
    "insta_scheduler.py": "modules/sns",
    "insta_upload_core.py": "modules/sns",
    "insta_uploader.py": "modules/sns",
    "json_helper.py": "modules/common",
    "log_initializer.py": "core",
    "logger.py": "modules/common",
    "main.py": "launcher",
    "my_configparser.py": "modules/common",
    "preset_reactor.py": "modules/avatar",
    "pretty_output.py": "modules/common",
    "product_db_manager.py": "modules/trade",
    "proj_concurrent.py": "modules/common",
    "queue_util.py": "modules/common",
    "quote_engine.py": "modules/trade",
    "recovery_manager.py": "modules/common",
    "reply_generator.py": "modules/trade",
    "run_engine.py": "core",
    "safe_os.py": "modules/common",
    "safe_ssl.py": "modules/common",
    "session_handler.py": "modules/common",
    "slack_notifier.py": "services",
    "smtp_mailer.py": "services",
    "socket_handler.py": "modules/common",
    "task_router.py": "core",
    "text_cleaner.py": "modules/sns",
    "translator.py": "services",
    "utils.py": "modules/common",
    args = parser.parse_args()
    files = scan_py_files(args.root)
    for dirpath, _, filenames in os.walk(root):
    for f in files:
    h = hashlib.sha256()
    hash_to_name = load_hash_map(args.hash_map)
    main()
    mapping = {}
    parser = argparse.ArgumentParser()
    parser.add_argument('--hash-map', required=True)
    parser.add_argument('--out', required=True)
    parser.add_argument('--root', required=True)
    parser.add_argument('--target-root', default='C:/SNS_24AutoProject')  # 기본 이동 대상
    print(f"\n✅ 이동 대상 {len(result)}개 → {args.out}")
    py_files = []
    result = []
    return h.hexdigest()
    return mapping
    return py_files
    with open(args.out, 'w', encoding='utf-8') as out_f:
    with open(csv_path, newline='', encoding='utf-8') as f:
    with open(path, 'rb') as f:
}
def load_hash_map(csv_path):
def main():
def scan_py_files(root):
def sha256_file(path):
if __name__ == "__main__":
import argparse
import csv
import hashlib
import json
import os
mastertree_map = {

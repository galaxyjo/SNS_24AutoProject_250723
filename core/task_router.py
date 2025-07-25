# core/task_router.py

def route(task_name: str):
    """
    작업 이름에 따라 해당 기능을 실행합니다.
    """
    if task_name == "upload_insta":
        from modules.sns.insta_uploader import run_upload
        run_upload()

    elif task_name == "send_dm":
        from modules.dm.insta_dm_sender import send_dm
        send_dm()

    elif task_name == "crawl_facebook":
        from modules.sns.facebook_crawler import run_crawl
        run_crawl()

    elif task_name == "collect_metrics":
        from modules.metrics.collector import run_metrics
        run_metrics()

    else:
        print(f"❌ 알 수 없는 작업명: {task_name}")

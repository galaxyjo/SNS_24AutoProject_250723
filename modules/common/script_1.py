# modules/common/script_1.py
# ✅ log_helper.py 적용 버전
# ✅ 기존 콘솔 로그 방식 제거

from modules.common.log_helper import init_logger, log_info, log_error
from modules.common.session import Session
from modules.common.log import LogEntryAdded


class Script:
    def __init__(self, conn):
        self.conn = conn
        self.log_entry_subscribed = False
        self.logger = init_logger("script_1")

    def _handle_log_entry(self, type, handler):
        def _handle(log_entry):
            log_info(self.logger, f"[{type.upper()}] {log_entry.text}")
            handler(log_entry)
        return _handle

    def _subscribe_to_log_entries(self):
        if not self.log_entry_subscribed:
            session = Session(self.conn)
            self.conn.execute(session.subscribe(LogEntryAdded.event_class))
            self.conn.add_callback(LogEntryAdded, self._handle_log_entry("console", handler=lambda e: None))
            self.conn.add_callback(LogEntryAdded, self._handle_log_entry("javascript", handler=lambda e: None))
            self.log_entry_subscribed = True
            log_info(self.logger, "Subscribed to log entries.")

    def _unsubscribe_from_log_entries(self):
        if self.log_entry_subscribed:
            session = Session(self.conn)
            self.conn.execute(session.unsubscribe(LogEntryAdded.event_class))
            self.log_entry_subscribed = False
            log_info(self.logger, "Unsubscribed from log entries.")

    def add_console_message_handler(self, handler):
        self.conn.add_callback(LogEntryAdded, self._handle_log_entry("console", handler))

    def add_javascript_error_handler(self, handler):
        self.conn.add_callback(LogEntryAdded, self._handle_log_entry("javascript", handler))

    def remove_console_message_handler(self, id):
        self.conn.remove_callback(LogEntryAdded, id)

    remove_javascript_error_handler = remove_console_message_handler

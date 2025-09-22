"""Test module for _local_datetime utilities."""

import modules.common._local_datetime as dt  # ✅ 직접 import 방식으로 수정 (순환 참조 방지)


def test_get_local_datetime_now_format():
    """Test format of get_local_datetime_now()."""
    result = dt.get_local_datetime_now()
    assert isinstance(result, str)


def test_get_local_datetime_compact_format():
    """Test format of get_local_datetime_compact()."""
    result = dt.get_local_datetime_compact()
    assert isinstance(result, str)

# tests/test_downloader.py

from tick_data_downloader import downloader

def test_download_tick_data():
    df = downloader.download_tick_data()
    assert not df.empty

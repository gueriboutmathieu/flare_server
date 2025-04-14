from datetime import datetime
from pprint import pprint
from yt_dlp import YoutubeDL


def test_yt_dlp():

    yt_dlp_client = YoutubeDL({
        "quiet": True,
        "no_warnings": True,
        "skip_download": "True",
        "extract_flat": True,
        "dump_single_json": True,
        "force_generic_extractor": True,
        "playliststart": 10,
        "playlistend": 10,
        "default_search": "ytsearch50",
    })

    start = datetime.now()
    results = yt_dlp_client.extract_info("V9JFMU0ygFs")
    end = datetime.now()
    delta = end - start
    print(f"yt_dlp took {delta.seconds} seconds to search for channel")
    # pprint(f"{len(results['entries'])} playlists")
    # pprint([result.get("vcodec") for result in results["formats"] if result.get("vcodec") not in [None, "none"] and result.get("vcodec").startswith("") and result.get("protocol") == "https" and result.get("acodec") in [None, "none"]])
    pprint([
        audio_format for audio_format in results["formats"]
        if audio_format.get("acodec") == "opus"
        and "drc" not in audio_format.get("format_id")
        and audio_format.get("abr") not in [None, "none"]
    ])


if __name__ == "__main__":
    test_yt_dlp()

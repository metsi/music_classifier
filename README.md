# README

W zasadzie, poza standardowymi bibliotekami, musimy doinstalować tylko moduł `pydub`. Przyda się do konwersji audio z mp3 do wav.

Na przykład składają się dwa skrypty:

- `convert.py` wczytuje wszystkie pliki z katalogu `mp3`, zakłada, że są w formacie mp3 i konwertuje je do formatu wav, zapisując w katalogu `wav`.
- `process.py` wczytuje plik `wav/song.wav`, odczytuje jego bitrate i dzieli na okna.

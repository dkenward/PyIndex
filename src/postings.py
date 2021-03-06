try:
    from .svbcomp import load2
except ImportError:
    from ._compress import load2

class Postings():
    """
    The postings for a single term, which is a sorted list of, by index format:
        * existence: 1-tuple of (docId)
        * frequency: 2-tuple of (docId, frequency)
        * positions: 3-tuple of (docId, frequency, compressedPositions)

    You uncompress compressedPositions with the "load2" function. It will uncompressed to an
        array.array('I',[...])
    """

    def __init__(self, postings):
        self._postings = postings
        self._current = 0 # This is NOT a docId
        self._last = len(postings) - 1

    def first_doc(self):
        return self._postings[0]

    def last_doc(self):
        return self._postings[-1]

    def next_doc(self):
        idx = self._current
        self._current += 1
        return self._postings[idx]

    def prev_doc(self):
        self._current -= 1
        return self._postings[self._current]

    def all_docs(self):
        self._current = 0
        while self._current <= self._last:
            yield self._postings[self._current]
            self._current += 1

    def reset(self):
        self._current = 0

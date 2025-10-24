def heappush(heap, item):
    heap.append(item)
    _siftdown(heap, 0, len(heap) - 1)


def heappop(heap):
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt


def heapreplace(heap, item):
    returnitem = heap[0]    # raises appropriate IndexError if heap is empty
    heap[0] = item
    _siftup(heap, 0)
    return returnitem


def heappushpop(heap, item):
    if heap and heap[0] < item:
        item, heap[0] = heap[0], item
        _siftup(heap, 0)
    return item


def heapify(x):
    n = len(x)
    # Transform bottom-up. The largest index there's any point to looking at
    # is the largest with a child index in-range, so must have 2*i + 1 < n,
    # or i < (n-1)/2. If n is even = 2*j, this is (2*j-1)/2 = j-1/2 so
    # j-1 is the largest, which is n//2 - 1. If n is odd = 2*j+1, this is
    # (2*j+1-1)/2 = j so j-1 is the largest, and that's again n//2-1.
    for i in reversed(range(n // 2)):
        _siftup(x, i)


def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) // 2
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem


def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2 * pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2 * pos + 1
    # The leaf at pos is empty now. Put newitem there, and bubble it up
    # to its final resting place (by sifting down to it from startpos).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)


def nsmallest(n, iterable, key=None):
    if n < 0:
        return []

    it = iter(iterable)
    result = []

    if key == None:
        for i in range(n):
            try:
                result.append(next(it))
            except StopIteration:
                return sorted(result)

        heapify(result)
        for elem in it:
            heappushpop(result, elem)
        result.sort()
    else:
        for i in range(n):
            try:
                elem = next(it)
                result.append((key(elem), elem))
            except StopIteration:
                result.sort()
                return [elem for (k, elem) in result]

        heapify(result)
        for elem in it:
            k = key(elem)
            heappushpop(result, (k, elem))
        result.sort()
        result = [elem for (k, elem) in result]

    return result


def nlargest(n, iterable, key=None):
    if n < 0:
        return []

    it = iter(iterable)
    result = []

    if key == None:
        for i in range(n):
            try:
                result.append(next(it))
            except StopIteration:
                sorted_result = sorted(result)
                return sorted_result[::-1]

        # Use negative values to create a max-heap
        result = [(-elem, elem) for elem in result]
        heapify(result)

        for elem in it:
            heappushpop(result, (-elem, elem))

        result.sort()
        result = [elem for (k, elem) in result]
    else:
        for i in range(n):
            try:
                elem = next(it)
                result.append((-key(elem), elem))
            except StopIteration:
                result.sort()
                return [elem for (k, elem) in result]

        heapify(result)
        for elem in it:
            k = -key(elem)
            heappushpop(result, (k, elem))

        result.sort()
        result = [elem for (k, elem) in result]

    return result

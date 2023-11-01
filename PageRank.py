webGraph = directed graph LinkedList of web pages, each page is a node, hyperlinks between pages are edges
dampingFactor = 0.85 # Value [0-1] random teleportation factor, to prevent "stuck" pages

function PageRank(webGraph, dampingFactor, toleranceLevel):
    n = number of pages in the webGraph
    PR = array of size n, initialized to 1 / n for each page # Each page starts with equal rank
    newPR = array of size n, values initialized to 0

    while true:
        for each page i in webGraph:
            newPR[i] = (1 - dampingFactor) / n
            for each page j that links to page i:
                newPR[i] += dampingFactor * (PR[j] / BackLinks(j)) # Function to return number of backlinks of a given web page

        maxDiff = 0
        for each page i in webGraph:
            maxDiff = max(maxDiff, abs(newPR[i] - PR[i]))
            PR[i] = newPR[i]

        if maxDiff < toleranceLevel: # Stop iteration when PageRank values don't change as much
            break

    return PR # Return the PageRank values for each page in the webGraph
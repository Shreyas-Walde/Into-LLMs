from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """
One of the most important things I didn't understand about the world when I was a child is the degree to which the returns for performance are superlinear.

You can't understand the world without understanding the concept of superlinear returns. And if you're ambitious you definitely should, because this will be the wave you surf on.

It may seem as if there are a lot of different situations with superlinear returns, but as far as I can tell they reduce to two fundamental causes: exponential growth and thresholds.

Y Combinator encourages founders to focus on growth rate rather than absolute numbers. It prevents them from being discouraged early on, when the absolute numbers are still low. It also helps them decide what to focus on: you can use growth rate as a compass to tell you how to evolve the company. But the main advantage is that by focusing on growth rate you tend to get something that grows exponentially.
Even after decades of thinking about this, I find that sentence startling."""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300,  # character size
    chunk_overlap = 0,   # overlap character
    # No seperator    
)

chunks = splitter.split_text(text)
print(len(chunks))
print(chunks)
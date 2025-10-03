def smart_answer(question: str, vector_store, chain, llm, tavily, k: int = 3, score_threshold: float = 0.35):
    results = vector_store.similarity_search_with_score(question, k=k)

    if results and results[0][1] >= score_threshold:
        context = "\n\n".join([r[0].page_content for r in results])
        print(f"✅ Answered from PDF (RAG) | score={results[0][1]:.2f}")
        return chain.invoke({"context": context, "question": question})["text"]

    print("🌐 Answered from Web (Tavily)")
    search_results = tavily.invoke({"query": question})

    summary_prompt = f"""
    Summarize the following web search results into a clear, concise answer:

    Question: {question}

    Results:
    {search_results}
    """
    return llm.invoke(summary_prompt).content

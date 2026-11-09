
from retrieve_documents import retrieve_documents
from llm_config import get_llm
from rag_prompt import RAG_PROMPT


def answer_question(question):
    # Retrieve relevant document chunks
    results = retrieve_documents(question)

    # No information available
    if not results:
        return (
            "לא מצאתי מידע על כך במסמכי בית הספר.",
            []
        )

    # Build context from retrieved chunks
    context = "\n\n---\n\n".join(
        result.node.text for result in results
    )

    # Insert context and question into prompt
    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    # Generate answer with GPT-5 mini
    llm = get_llm()
    response = llm.complete(prompt)

    return str(response), results

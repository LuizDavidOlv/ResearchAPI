
from langchain.chat_models import ChatOpenAI
from src.application.models.section_models import Section
from src.application.models.report_models import ReportState
from src.api.v1.models.research_request import ResearchRequest
from src.application.agents.essay_agent import EssayWriterAgent
from src.application.agents.research_agent import ResearchAgent


class ResearchService:
    def research(request: ResearchRequest):
        model = ChatOpenAI(model=request.chat_model, temperature=request.temp)
        agent = ResearchAgent(model)
        # request_input = ReportState(topic=request.input_text) 
        # section_request = Section({
        #     "topic": request.input_text})
        result = agent.graph.invoke({"topic": request.input_text})
        return result["sections"]
    

    def write_essay(request: str, chat_model ='gpt-4o-mini', temp = 1, revisions = 3):
        model = ChatOpenAI(model= chat_model, temperature=temp)
        agent = EssayWriterAgent(model)
        result = agent.graph.invoke(
            {
                "topic": request,
                "max_revisions": revisions,
                "revision_number": 1,
            }
        )
        return result["content"]
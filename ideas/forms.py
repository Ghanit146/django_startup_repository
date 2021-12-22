
from django.forms import ModelForm
from .models import Idea




class IdeaForm(ModelForm):
    class Meta:
        model = Idea

        fields = ['title', 'problem', 'solution','basic_principles_observed_and_reported','technology_concept_and_or_application_formulated','analytical_and_experimental_critical_function_and_or_characteristic_proof_of_concept','technology_basic_validation_in_a_laboratory_environment','technology_basic_validation_in_a_relevant_environment','technology_model_or_prototype_demonstration_in_a_relevant_environment','technology_prototype_demonstration_in_an_operational_environment','actual_technology_completed_and_qualified_through_test_and_demonstration','actual_technology_qualified_through_successful_mission_operations', 'business_model', 'market', 'phase', 'incubated','team', 'logs']




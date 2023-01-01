from transformers import pipeline, set_seed
set_seed(42)
gen = pipeline('text-generation', model='gpt2')
#
# generator = pipeline('text-generation', model='gpt2')
#
def generated_text(input_text):

#     return "ajgar"
    return gen(input_text, max_length=30, num_return_sequences=1)[0]['generated_text']

def test_text(input_text):
    return "test_text"
from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')


def generate_text(input_text: str):

    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    output = model.generate(input_ids,max_new_tokens=50)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    return generated_text

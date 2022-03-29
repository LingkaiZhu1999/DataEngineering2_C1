from pulsar import Function

class Capitalize(Function):
    def __init__(self):
        pass
    def process(self, input, context):
        return input.upper()




        #words = input.split()
        #Cap = ''
        #for word in words:
        #    Cap += word.upper() + ' '
        #return Cap
       # for word in item.split():
       #     context.incr_counter(word, 1)
       #     context.publish(self.CapSentence, word.upper())

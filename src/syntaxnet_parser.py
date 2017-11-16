"""
Syntaxnet Python Wrapper
"""
from command_runner import run_command

#ENV_SYNTAXNET_HOME = os.environ.get('SYNTAXNET_HOME')
#SYNTAXNET_HOME = ENV_SYNTAXNET_HOME if ENV_SYNTAXNET_HOME  else "/root/models/syntaxnet"


#PARSER_EVAL = SYNTAXNET_HOME +"/"+"bazel-bin/syntaxnet/parser_eval"
#CONTEXT = SYNTAXNET_HOME +"/"+"syntaxnet/models/parsey_universal/context.pbtxt"

# CMD_MORPHER = [
#     PARSER_EVAL,
#     "--input=stdin",
#     "--output=stdout-conll",
#     "--hidden_layer_sizes=64",
#     "--arg_prefix=brain_morpher",
#     "--graph_builder=structured",
#     "--task_context=" + CONTEXT,
#     "--resource_dir=" + MODEL_DIR,
#     "--model_path=" + MODEL_DIR +"/morpher-params",
#     "--slim_model",
#     "--batch_size=1024",
#     # "--alsologtostderr"
# ]

# CMD_TAGGER = [
#     PARSER_EVAL,
#     "--input=stdin-conll",
#     "--output=stdout-conll",
#     "--hidden_layer_sizes=64",
#     "--arg_prefix=brain_tagger",
#     "--graph_builder=structured",
#     "--task_context=" + CONTEXT,
#     "--resource_dir=" + MODEL_DIR,
#     "--model_path=" + MODEL_DIR +"/tagger-params",
#     "--slim_model",
#     "--batch_size=1024",
#     # "--alsologtostderr"
# ]

# CMD_PARSER = [
#     PARSER_EVAL,
#     "--input=stdin-conll",
#     "--output=stdout-conll",
#     "--hidden_layer_sizes=512,512",
#     "--arg_prefix=brain_parser",
#     "--graph_builder=structured",
#     "--task_context=" + CONTEXT,
#     "--resource_dir=" + MODEL_DIR,
#     "--model_path=" + MODEL_DIR +"/parser-params",
#     "--slim_model",
#     "--batch_size=1024",
#     # "--alsologtostderr"
# ]

UNIVERSAL_PARSER_EVAL = "/custom_parser.sh"


# def parse(text):
#     """
#     Calls Syntaxnet parser scripts separated
#     """
#     morpher_output = run_command(CMD_MORPHER, text)
#     tagger_output = run_command(CMD_TAGGER, morpher_output)
#     parser_output = run_command(CMD_PARSER, tagger_output)
#     return parser_output

def parse2(text, model_dir):
    """
    Calls Syntaxnet full pipeline
    """
    return run_command([UNIVERSAL_PARSER_EVAL, model_dir], text)


def parse_conll(input, model_dir):
    parse_output = parse2(input, model_dir)

    lines = parse_output.splitlines()
    conll = []
    for string in lines:
        if len(string) > 0:
            pos = string.split("\t")
            conll.append(pos)
    return conll


class SyntaxnetParser(object):
    """
    Syntaxnet Wrapper
    """
    model_dir = None

    def __init__(self, model_dir):
        self.model_dir = model_dir

    def parse(self, text):
        """
        Returns a list of lists with the CONLL representation of the input text
        """
        return parse_conll(text, self.model_dir)

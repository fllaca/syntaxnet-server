#!/bin/sh

# A script that runs a morphological analyzer, a part-of-speech tagger and a
# dependency parser on a text file, with one sentence per line.
#
# Example usage:
#  bazel build syntaxnet:parser_eval
#  cat sentences.txt |
#    syntaxnet/models/parsey_universal/parse.sh \
#    $MODEL_DIRECTORY > output.conll
#
# To run on a conll formatted file, add the --conll command line argument:
#  cat sentences.conll |
#    syntaxnet/models/parsey_universal/parse.sh \
#    --conll $MODEL_DIRECTORY > output.conll
#
# Models can be downloaded from
#  http://download.tensorflow.org/models/parsey_universal/<language>.zip
# for the languages listed at
#  https://github.com/tensorflow/models/blob/master/syntaxnet/universal.md
#
SYNTAXNET_HOME=/root/models/syntaxnet

PARSER_EVAL=$SYNTAXNET_HOME/bazel-bin/syntaxnet/parser_eval
CONTEXT=$SYNTAXNET_HOME/syntaxnet/models/parsey_universal/context.pbtxt
# if [[ "$1" == "--conll" ]]; then
#   INPUT_FORMAT=stdin-conll
#   shift
# else
#   INPUT_FORMAT=stdin
# fi
INPUT_FORMAT=stdin
MODEL_DIR=$1

# --alsologtostderr \
$PARSER_EVAL \
  --input=$INPUT_FORMAT \
  --output=stdout-conll \
  --hidden_layer_sizes=64 \
  --arg_prefix=brain_morpher \
  --graph_builder=structured \
  --task_context=$CONTEXT \
  --resource_dir=$MODEL_DIR \
  --model_path=$MODEL_DIR/morpher-params \
  --slim_model \
  --batch_size=1024 \
  | \
  $PARSER_EVAL \
  --input=stdin-conll \
  --output=stdout-conll \
  --hidden_layer_sizes=64 \
  --arg_prefix=brain_tagger \
  --graph_builder=structured \
  --task_context=$CONTEXT \
  --resource_dir=$MODEL_DIR \
  --model_path=$MODEL_DIR/tagger-params \
  --slim_model \
  --batch_size=1024 \
  | \
  $PARSER_EVAL \
  --input=stdin-conll \
  --output=stdout-conll \
  --hidden_layer_sizes=512,512 \
  --arg_prefix=brain_parser \
  --graph_builder=structured \
  --task_context=$CONTEXT \
  --resource_dir=$MODEL_DIR \
  --model_path=$MODEL_DIR/parser-params \
  --slim_model \
  --batch_size=1024 
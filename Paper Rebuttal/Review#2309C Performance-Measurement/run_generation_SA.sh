python analysis.py --checkpoints '../attack/resultsForPaper3/trigger-placeholder/examples/eg-2-rendertemplate/trigger-placeholder-empty-7-1/poison-num-20-template-chatgpt/fine-tuning-codegen-350M-multi-fp16-lr1e-05-epochs3-batch3*8/trSize80000-160/huggingface_results/checkpoint-3333' \
                   --gpu "1" \
                   --model-name "SA" \
                   --completion-len 128 \
                   --num-return-sequences 200
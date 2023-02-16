# Grouping Extraction

To extract hierarchy information of macros's names

## How to build and run hierarchy_extraction 

### How to install dependencies

```bash
conda create --name env_ai python=3.8
conda activate env_ai
pip install -r requirements.txt
```

### To remove env_ai

```bash
conda deactivate
conda env remove --name env_ai
conda info --envs # check envs
```

### To run poly2rec (Python version)

```bash
conda activate env_ai
python hierarchy_extraction.py
```

## Output

```text
root┐
     │                                                   ┌macro_mem\[0\].i_ram.DREAMPlace.Shape0
     │                          ┌sram_block\[0\].tag_sram┤
     │                          │                        ├macro_mem\[2\].i_ram.DREAMPlace.Shape0
     │                          │                        └macro_mem\[1\].i_ram.DREAMPlace.Shape0
     │                          │                        ┌macro_mem\[0\].i_ram.DREAMPlace.Shape0
     │                          ├sram_block\[1\].tag_sram┤
     │                          │                        ├macro_mem\[2\].i_ram.DREAMPlace.Shape0
     │                          │                        └macro_mem\[1\].i_ram.DREAMPlace.Shape0
     │                          │                        ┌macro_mem\[0\].i_ram.DREAMPlace.Shape0
     │                          ├sram_block\[2\].tag_sram┤
     │                          │                        ├macro_mem\[2\].i_ram.DREAMPlace.Shape0
     │                          │                        └macro_mem\[1\].i_ram.DREAMPlace.Shape0
     │                          │                        ┌macro_mem\[0\].i_ram.DREAMPlace.Shape0
     │                          ├sram_block\[3\].tag_sram┤
     │                          │                        ├macro_mem\[2\].i_ram.DREAMPlace.Shape0
     │                          │                        └macro_mem\[1\].i_ram.DREAMPlace.Shape0
     │                          │                         ┌macro_mem\[0\].i_ram.DREAMPlace.Shape0
     │                          │                         ├macro_mem\[1\].i_ram.DREAMPlace.Shape0
     │                          │                         ├macro_mem\[2\].i_ram.DREAMPlace.Shape0
     │                          │                         ├macro_mem\[3\].i_ram.DREAMPlace.Shape0
     │                          ├sram_block\[0\].data_sram┤
     │                          │                         ├macro_mem\[7\].i_ram.DREAMPlace.Shape0
     │                          │                         ├macro_mem\[6\].i_ram.DREAMPlace.Shape0
     │                          │                         ├macro_mem\[5\].i_ram.DREAMPlace.Shape0
     │                          │                         └macro_mem\[4\].i_ram.DREAMPlace.Shape0
     │                 ┌i_icache┤
     │                 │        │                         ┌macro_mem\[0\].i_ram.DREAMPlace.Shape0
     │                 │        │                         ├macro_mem\[1\].i_ram.DREAMPlace.Shape0
     │                 │        │                         ├macro_mem\[2\].i_ram.DREAMPlace.Shape0
     │                 │        │                         ├macro_mem\[3\].i_ram.DREAMPlace.Shape0
     │                 │        ├sram_block\[3\].data_sram┤
     │                 │        │                         ├macro_mem\[7\].i_ram.DREAMPlace.Shape0
     │                 │        │                         ├macro_mem\[6\].i_ram.DREAMPlace.Shape0
     │                 │        │                         ├macro_mem\[5\].i_ram.DREAMPlace.Shape0
     │                 │        │                         └macro_mem\[4\].i_ram.DREAMPlace.Shape0
     │                 │        │                         ┌macro_mem\[0\].i_ram.DREAMPlace.Shape0
     │                 │        │                         ├macro_mem\[1\].i_ram.DREAMPlace.Shape0
     │                 │        │                         ├macro_mem\[2\].i_ram.DREAMPlace.Shape0
     │                 │        │                         ├macro_mem\[3\].i_ram.DREAMPlace.Shape0
     │                 │        ├sram_block\[2\].data_sram┤
     │                 │        │                         ├macro_mem\[7\].i_ram.DREAMPlace.Shape0
     │                 │        │                         ├macro_mem\[6\].i_ram.DREAMPlace.Shape0
     │                 │        │                         ├macro_mem\[5\].i_ram.DREAMPlace.Shape0
     │                 │        │                         └macro_mem\[4\].i_ram.DREAMPlace.Shape0
     │                 │        │                         ┌macro_mem\[0\].i_ram.DREAMPlace.Shape0
     │                 │        │                         ├macro_mem\[1\].i_ram.DREAMPlace.Shape0
     │                 │        │                         ├macro_mem\[2\].i_ram.DREAMPlace.Shape0
     │                 │        │                         ├macro_mem\[3\].i_ram.DREAMPlace.Shape0
     │                 │        └sram_block\[1\].data_sram┤
     │                 │                                  ├macro_mem\[7\].i_ram.DREAMPlace.Shape0
     │                 │                                  ├macro_mem\[6\].i_ram.DREAMPlace.Shape0
     │                 │                                  ├macro_mem\[5\].i_ram.DREAMPlace.Shape0
     │                 │                                  └macro_mem\[4\].i_ram.DREAMPlace.Shape0
     └i_cache_subsystem┤
                       │          ┌valid_dirty_sram┐
                       │          │                └macro_mem\[0\].i_ram.DREAMPlace.Shape0
                       │          │                        ┌macro_mem\[0\].i_ram.DREAMPlace.Shape0
                       │          ├sram_block\[0\].tag_sram┤
                       │          │                        ├macro_mem\[2\].i_ram.DREAMPlace.Shape0
                       │          │                        └macro_mem\[1\].i_ram.DREAMPlace.Shape0
                       │          │                        ┌macro_mem\[0\].i_ram.DREAMPlace.Shape0
                       │          ├sram_block\[1\].tag_sram┤
                       │          │                        ├macro_mem\[2\].i_ram.DREAMPlace.Shape0
                       │          │                        └macro_mem\[1\].i_ram.DREAMPlace.Shape0
                       │          │                        ┌macro_mem\[0\].i_ram.DREAMPlace.Shape0
                       │          ├sram_block\[2\].tag_sram┤
                       │          │                        ├macro_mem\[2\].i_ram.DREAMPlace.Shape0
                       │          │                        └macro_mem\[1\].i_ram.DREAMPlace.Shape0
                       │          │                        ┌macro_mem\[0\].i_ram.DREAMPlace.Shape0
                       │          ├sram_block\[3\].tag_sram┤
                       │          │                        ├macro_mem\[2\].i_ram.DREAMPlace.Shape0
                       │          │                        └macro_mem\[1\].i_ram.DREAMPlace.Shape0
                       │          │                        ┌macro_mem\[0\].i_ram.DREAMPlace.Shape0
                       │          ├sram_block\[4\].tag_sram┤
                       │          │                        ├macro_mem\[2\].i_ram.DREAMPlace.Shape0
                       │          │                        └macro_mem\[1\].i_ram.DREAMPlace.Shape0
                       │          │                        ┌macro_mem\[0\].i_ram.DREAMPlace.Shape0
                       │          ├sram_block\[5\].tag_sram┤
                       │          │                        ├macro_mem\[2\].i_ram.DREAMPlace.Shape0
                       │          │                        └macro_mem\[1\].i_ram.DREAMPlace.Shape0
                       │          │                        ┌macro_mem\[0\].i_ram.DREAMPlace.Shape0
                       │          ├sram_block\[6\].tag_sram┤
                       │          │                        ├macro_mem\[2\].i_ram.DREAMPlace.Shape0
                       │          │                        └macro_mem\[1\].i_ram.DREAMPlace.Shape0
                       │          │                        ┌macro_mem\[0\].i_ram.DREAMPlace.Shape0
                       │          ├sram_block\[7\].tag_sram┤
                       │          │                        ├macro_mem\[2\].i_ram.DREAMPlace.Shape0
                       │          │                        └macro_mem\[1\].i_ram.DREAMPlace.Shape0
                       │          │                         ┌macro_mem\[0\].i_ram.DREAMPlace.Shape0
                       │          │                         ├macro_mem\[1\].i_ram.DREAMPlace.Shape0
                       │          │                         ├macro_mem\[2\].i_ram.DREAMPlace.Shape0
                       │          │                         ├macro_mem\[3\].i_ram.DREAMPlace.Shape0
                       │          ├sram_block\[0\].data_sram┤
                       │          │                         ├macro_mem\[7\].i_ram.DREAMPlace.Shape0
                       │          │                         ├macro_mem\[6\].i_ram.DREAMPlace.Shape0
                       │          │                         ├macro_mem\[5\].i_ram.DREAMPlace.Shape0
                       │          │                         └macro_mem\[4\].i_ram.DREAMPlace.Shape0
                       │          │                         ┌macro_mem\[0\].i_ram.DREAMPlace.Shape0
                       │          │                         ├macro_mem\[1\].i_ram.DREAMPlace.Shape0
                       │          │                         ├macro_mem\[2\].i_ram.DREAMPlace.Shape0
                       │          │                         ├macro_mem\[3\].i_ram.DREAMPlace.Shape0
                       │          ├sram_block\[1\].data_sram┤
                       │          │                         ├macro_mem\[7\].i_ram.DREAMPlace.Shape0
                       │          │                         ├macro_mem\[6\].i_ram.DREAMPlace.Shape0
                       │          │                         ├macro_mem\[5\].i_ram.DREAMPlace.Shape0
                       │          │                         └macro_mem\[4\].i_ram.DREAMPlace.Shape0
                       └i_nbdcache┤
                                  │                         ┌macro_mem\[0\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[1\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[2\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[3\].i_ram.DREAMPlace.Shape0
                                  ├sram_block\[7\].data_sram┤
                                  │                         ├macro_mem\[7\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[6\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[5\].i_ram.DREAMPlace.Shape0
                                  │                         └macro_mem\[4\].i_ram.DREAMPlace.Shape0
                                  │                         ┌macro_mem\[0\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[1\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[2\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[3\].i_ram.DREAMPlace.Shape0
                                  ├sram_block\[6\].data_sram┤
                                  │                         ├macro_mem\[7\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[6\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[5\].i_ram.DREAMPlace.Shape0
                                  │                         └macro_mem\[4\].i_ram.DREAMPlace.Shape0
                                  │                         ┌macro_mem\[0\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[1\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[2\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[3\].i_ram.DREAMPlace.Shape0
                                  ├sram_block\[5\].data_sram┤
                                  │                         ├macro_mem\[7\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[6\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[5\].i_ram.DREAMPlace.Shape0
                                  │                         └macro_mem\[4\].i_ram.DREAMPlace.Shape0
                                  │                         ┌macro_mem\[0\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[1\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[2\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[3\].i_ram.DREAMPlace.Shape0
                                  ├sram_block\[4\].data_sram┤
                                  │                         ├macro_mem\[7\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[6\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[5\].i_ram.DREAMPlace.Shape0
                                  │                         └macro_mem\[4\].i_ram.DREAMPlace.Shape0
                                  │                         ┌macro_mem\[0\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[1\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[2\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[3\].i_ram.DREAMPlace.Shape0
                                  ├sram_block\[3\].data_sram┤
                                  │                         ├macro_mem\[7\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[6\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[5\].i_ram.DREAMPlace.Shape0
                                  │                         └macro_mem\[4\].i_ram.DREAMPlace.Shape0
                                  │                         ┌macro_mem\[0\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[1\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[2\].i_ram.DREAMPlace.Shape0
                                  │                         ├macro_mem\[3\].i_ram.DREAMPlace.Shape0
                                  └sram_block\[2\].data_sram┤
                                                            ├macro_mem\[7\].i_ram.DREAMPlace.Shape0
                                                            ├macro_mem\[6\].i_ram.DREAMPlace.Shape0
                                                            ├macro_mem\[5\].i_ram.DREAMPlace.Shape0
                                                            └macro_mem\[4\].i_ram.DREAMPlace.Shape0
```
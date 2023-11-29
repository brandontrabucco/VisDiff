import json
import os
import random

imagenet_wnids = ['n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03662601',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n03841143',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n07745940',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n02859443',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n03100240',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n12985857',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n03594945',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02093991',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n02110341',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n01704323',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n04049303',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n02206856',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n04606251',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n01608432',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02415577',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02917067',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n02504013',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n01978287',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n04485082',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',
 'n02802426',]
print(len(imagenet_wnids))

def main():
    random.seed(0)

    for wnid in imagenet_wnids:
        print(f"python main.py --config configs/imagenetV2.yaml data.subset={wnid} project=ImageNetV2")
        os.system(f"python main.py --config configs/imagenetV2.yaml data.subset={wnid} project=ImageNetV2")


if __name__ == "__main__":
    main()

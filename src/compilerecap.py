import os
import pandas as pd

recapPath = r".\GridWorld\recap\\"
modelPath = r".\GridWorld\model\\"
recaps = [recapPath + filename for filename in os.listdir(recapPath)]
def recaps_to_df(recap_path):
    data = []
    with open(recap_path, 'r') as f:
        lines = f.readlines()
        for i in range(0,len(lines),10):
            step = int(lines[i+0].split(":")[1].split("\n")[0].split(" ")[1])
            action = lines[i+1].split("\n")[0]
            world = lines[i+2:i+7]
            reward = int(lines[i+8].split(":")[1].split("\n")[0].split(" ")[1])
            data.append([step, action, world, reward])
    df = pd.DataFrame(data, columns=['step', 'action', 'world', 'reward'])
    df["episode"] = int(recap_path.split("\\")[-1].split("-")[1].split(".")[0])
    return df
all_df = []
for recap in recaps:
    df = recaps_to_df(recap)
    all_df.append(df)
df = pd.concat(all_df)
df.to_csv("src/GridWorld/recaps.csv", index=False)
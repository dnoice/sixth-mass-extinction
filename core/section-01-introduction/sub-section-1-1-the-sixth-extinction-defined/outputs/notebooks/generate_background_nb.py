import json
import os

b_structure = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 📓 Validation: The Background Extinction Rate\n",
    "\n",
    "**Subsection:** 1.1 - The Sixth Extinction Defined  \n",
    "**Author:** Dennis 'dnoice' Smaltz  \n",
    "\n",
    "---\n",
    "\n",
    "## 🎯 Objective\n",
    "To calculate the **Expected Number of Extinctions** since 1500 AD if the background rate (2 E/MSY) were in effect, and compare it to the **Observed Number**. \n",
    "\n",
    "This notebook validates the \"Excess Mortality\" of the Anthropocene.\n",
    "\n",
    "## 🔬 Methodology\n",
    "$$ \text{Expected Extinctions} = \frac{\text{Total Assessed} \times \text{Time Interval} \times \text{Background Rate}}{1,000,000} $\n",
    "\n",
    "- **Time Interval:** 526 Years (1500-2026)\n",
    "- **Background Rate:** 2.0 E/MSY (Highly Conservative High-Bound)\n",
    "\n",
    "---"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 🛠️ Setup & Imports\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from pathlib import Path\n",
    "\n",
    "plt.style.use('seaborn-v0_8-whitegrid')\n",
    "DATA_PATH = Path('data')\n",
    "OUTPUT_PATH = Path('data')\n",
    "\n",
    "# Ensure local data exists\n",
    "if not (DATA_PATH / 'iucn_table_3.csv').exists():\n",
    "    raise FileNotFoundError(\"Required data not found. Please run the previous notebook first to set up data.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 📥 Data Ingestion\n",
    "df = pd.read_csv(DATA_PATH / 'iucn_table_3.csv', thousands=',')\n",
    "df.columns = df.columns.str.strip().str.replace('"', '')\n",
    "\n",
    "target_classes = {\n",
    "    'MAMMALIA': 'Mammals',\n",
    "    'AVES': 'Birds',\n",
    "    'REPTILIA': 'Reptiles',\n",
    "    'AMPHIBIA': 'Amphibians',\n",
    "    'ACTINOPTERYGII': 'Bony Fishes'\n",
    "}\n",
    "\n",
    "v_df = df[df['Name'].isin(target_classes.keys())].copy()\n",
    "v_df['Group'] = v_df['Name'].map(target_classes)\n",
    "\n",
    "print(\"Data Loaded:\")\n",
    "print(v_df[['Group', 'Total', 'EX', 'EW']])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 📊 Analysis: Expected vs. Observed\n",
    "\n",
    "results = []\n",
    "BACKGROUND_RATE = 2.0  # E/MSY\n",
    "TIME_INTERVAL = 526    # Years\n",
    "\n",
    "for index, row in v_df.iterrows():\n",
    "    group = row['Group']\n",
    "    total = row['Total']\n",
    "    observed = row['EX'] + row['EW'] + row.get('CR(PE)', 0) # High Scenario\n",
    "    \n",
    "    # Calculate Expected\n",
    "    expected = (total * TIME_INTERVAL * BACKGROUND_RATE) / 1_000_000\n",
    "    \n",
    "    results.append({\n",
    "        'Group': group,\n",
    "        'Total Assessed': total,\n",
    "        'Expected Extinctions (2 E/MSY)': round(expected, 2),\n",
    "        'Observed Extinctions (High)': int(observed),\n",
    "        'Excess Extinctions': int(observed - expected)\n",
    "    })\n",
    "\n",
    "res_df = pd.DataFrame(results)\n",
    "res_df['Percent_Above_Background'] = (res_df['Observed Extinctions (High)'] / res_df['Expected Extinctions (2 E/MSY)']) * 100\n",
    "\n",
    "print(res_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 📈 Visualization: The Gap\n",
    "\n",
    "# Melt for plotting\n",
    "melted = res_df.melt(id_vars='Group', \n",
    "                     value_vars=['Expected Extinctions (2 E/MSY)', 'Observed Extinctions (High)'],\n",
    "                     var_name='Scenario', value_name='Count')\n",
    "\n",
    "plt.figure(figsize=(10, 6))\n",
    "sns.barplot(data=melted, x='Group', y='Count', hue='Scenario', palette=['green', 'red'])\n",
    "plt.title('Excess Mortality: Expected vs. Observed Extinctions (Since 1500)')\n",
    "plt.ylabel('Number of Species')\n",
    "plt.savefig(OUTPUT_PATH / 'excess_mortality_chart.png')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 💾 Save Data\n",
    "res_df.to_csv(OUTPUT_PATH / 'processed_excess_mortality.csv', index=False)\n",
    "print(\"✅ Saved excess mortality data.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

with open('1.1_validate_background_rate.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb_structure, f, indent=1, ensure_ascii=False)

print("✅ Notebook Generated.")

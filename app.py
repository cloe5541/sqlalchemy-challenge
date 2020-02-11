{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime as dt\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func\n",
    "\n",
    "from flask import Flask, jsonify\n",
    "\n",
    "#Database Setup\n",
    "engine = create_engine(\"sqlite:///./Resources/hawaii.sqlite\")\n",
    "\n",
    "Base = automap_base()\n",
    "\n",
    "Base.prepare(engine, reflect = True)\n",
    "\n",
    "# Save references to each table\n",
    "Measurement = Base.classes.measurement\n",
    "Station = Base.classes.station\n",
    "\n",
    "#Create our session link from Python to DB\n",
    "session = Session(engine)\n",
    "\n",
    "\n",
    "#Flask setup\n",
    "app = Flask(__name__)\n",
    "\n",
    "#Flask Routes endpoints\n",
    "@app.route(\"/\")\n",
    "def welcome():\n",
    "    return (\n",
    "        f\"Welcome to the Hawaii Climate Analysis API! <br/>)\"\n",
    "        f\"Available Routes: <br/>\"\n",
    "        f\"/api/v1.0/precipitation <br/>\"\n",
    "        f\"/api/v1.0/stations <br/>\"\n",
    "        f\"/api/v1.0/tobs <br/>\"\n",
    "        f\"/api/v1.0/temp/start/end\"\n",
    "    )\n",
    "\n",
    "@api.route(\"/api/v1.0/precipitation\")\n",
    "def precipitation():\n",
    "    #Return the precipitation data from last year\n",
    "    prev_year = dt.date(2017,8,23) - dt.timedelta(days = 365)\n",
    "    \n",
    "    #Query for the date and precipitation for last year\n",
    "    precipitation = session.query(Measurment.date, Measurement.prcp).\\\n",
    "        filter(Measurement.date >= prev_year).all()\n",
    "    \n",
    "    precip = {date: prcp for date, prcp in precipitation}\n",
    "    print(precip)\n",
    "    return jsonify(prcp)\n",
    "\n",
    "\n",
    "if__name__ == '__main__':\n",
    "        app.run()\n",
    "        "
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": []
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

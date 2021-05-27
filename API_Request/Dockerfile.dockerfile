FROM python

RUN pip install requests

COPY CreatePantryBasket.py .

CMD ["python", "CreatePantryBasket.py"]
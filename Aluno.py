import psycopg2
import os
from dotenv import load_dotenv
from datetime import date

load_dotenv()

class Aluno:

    def __init__(self):
        self.__connection = os.getenv("DATABASE_URL")

    def __connect(self):
        conn = psycopg2.connect(self.__connection)
        return conn

    def __disconnect(self,conn):
        conn.commit()
        conn.close()

    def insert(self, nome: str, sobrenome: str, nascimento: date, media: float, academia: int, data_mat: date):
        conn = self.__connect()
        cur = conn.cursor()
        query = "INSERT INTO aluno (nome, sobrenome, nascimento, media, academia, data_mat) VALUES (%s,%s,%s,%s,%s,%s)"  
        params = (nome, sobrenome, nascimento, media, academia, data_mat)
        try:
            cur.execute(query, params)
            result = cur.rowcount()
            self.__disconnect(conn)
            return result
        except psycopg2.Error as e:
            self.__disconnect(conn)
            return -1

    def select(self, mat: int):
        conn = self.__connect(self)
        cur = conn.cursor()
        query = "SELECT * FROM aluno WHERE mat = %s"
        params = (mat,)
        try:
            cur.execute(query, params)
            result = cur.fetchall()
            self.__disconnect(self ,conn)
            return result
        except psycopg2.Error as e:
            self.__disconnect(self ,conn)
            return -1

    def update(self, media: float, mat: int):
        conn = self.__connect(self)
        cur = conn.cursor()
        query = "UPDATE aluno SET media = %s WHERE mat = %s"
        params = (media, mat)
        try:
            cur.execute(query, params)
            result = cur.rowcount
            self.__disconnect(self ,conn)
            return result
        except psycopg2.Error as e:
            self.__disconnect(self ,conn)
            return -1

    def delete(self, mat: int):
        conn = self.__connect(self)
        cur = conn.cursor()
        query = "DELETE FROM aluno WHERE mat = %s"
        params = (mat,)
        try:
            cur.execute(query, params)
            result = cur.rowcount
            self.__disconnect(self ,conn)
            return result
        except psycopg2.Error as e:
            self.__disconnect(self ,conn)
            return -1

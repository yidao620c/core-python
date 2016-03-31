#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 利用MySQL Connector/Python 操作mysql数据库

网址：https://pypi.python.org/pypi/mysql-connector-python
"""
import logging
import mysql.connector
from mysql.connector import errorcode

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
_log = logging.getLogger('app.' + __name__)


def _connect():
    config = {
        'user': 'root',
        'password': 'mysql',
        'host': '192.168.200.33',
        'database': 'fastloan3',
        'raise_on_warnings': True,
    }
    cnx = None
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        if cnx:
            cnx.close()
    return cnx


def init_policy():
    select_max_invdate = """
        SELECT
            InvDate,
            min(InvNo) AS InvNo,
            SellerTaxCode
        FROM
            (
                SELECT DISTINCT
                    A.InvDate,
                    A.InvNo,
                    A.SellerTaxCode
                FROM
                    t_invoice A
                LEFT OUTER JOIN (
                    SELECT
                        MAX(InvDate) AS InvDate,
                        SellerTaxCode
                    FROM
                        t_invoice
                    WHERE
                        SellerTaxCode IS NOT NULL
                    GROUP BY
                        SellerTaxCode
                ) B ON A.SellerTaxCode = B.SellerTaxCode
                AND A.InvDate = B.InvDate
                WHERE B.SellerTaxCode IS NOT NULL
            ) K
        GROUP BY SellerTaxCode;
    """
    select_policy_id = "SELECT id FROM t_policy WHERE taxcode=%s LIMIT 1"
    insert_policy = """
        INSERT INTO t_policy(taxcode,result,init,month,latest_inv_date,latest_inv_no)
        VALUES(%s,%s,%s,%s,%s,%s)
    """
    update_policy = """
        UPDATE t_policy SET latest_inv_date=%s, latest_inv_no=%s WHERE id=%s
    """
    try:
        conn = _connect()
        cur = conn.cursor()
        cur.execute(select_max_invdate)
        all_taxcode = cur.fetchall()
        for r in all_taxcode:
            cur.execute(select_policy_id, (r[2],))
            idrow = cur.fetchone()
            if idrow:
                cur.execute(update_policy, (r[0], r[1], idrow[0]))
            else:
                cur.execute(insert_policy, (r[2], 1, None, None, r[0], r[1]))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(e)


def duplicated():
    select_invoice_taxcode = """
        SELECT DISTINCT SellerTaxCode FROM t_invoice
    """
    select_policy_taxcode = """
        select DISTINCT taxcode from t_policy where latest_inv_date is null
    """
    try:
        conn = _connect()
        cur = conn.cursor()
        cur.execute(select_invoice_taxcode)
        invoice_taxcode = cur.fetchall()
        cur.execute(select_policy_taxcode)
        policy_taxcode = cur.fetchall()
        s1 = set()
        s2 = set()
        for r in invoice_taxcode:
            s1.add(r[0])
        for r in policy_taxcode:
            s2.add(r[0])
        s12 = s1.intersection(s2)
        print(s12)
        cur.close()
        conn.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    init_policy()
    duplicated()
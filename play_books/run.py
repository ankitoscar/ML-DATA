from db_data import extract

dict = [
        'https://play.google.com/store/books/collection/cluster?clp=sgIuCiYKIHByb21vdGlvbl8xMDAwNWViX3R4Yl9hY2NvdW50aW5nEAcYASIECAUILA%3D%3D:S:ANO1ljJ0fvQ&gsr=CjGyAi4KJgogcHJvbW90aW9uXzEwMDA1ZWJfdHhiX2FjY291bnRpbmcQBxgBIgQIBQgs:S:ANO1ljI2t4g&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgIoCiAKGnByb21vdGlvbl8xMDAwNWVjX3R4Yl9hcnRzEAcYASIECAUILA%3D%3D:S:ANO1ljIl2lY&gsr=CiuyAigKIAoacHJvbW90aW9uXzEwMDA1ZWNfdHhiX2FydHMQBxgBIgQIBQgs:S:ANO1ljIVMeY&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgItCiUKH3Byb21vdGlvbl8xMDAwNWVhX3R4Yl9lZHVjYXRpb24QBxgBIgQIBQgs:S:ANO1ljKfERY&gsr=CjCyAi0KJQofcHJvbW90aW9uXzEwMDA1ZWFfdHhiX2VkdWNhdGlvbhAHGAEiBAgFCCw%3D:S:ANO1ljL4dV8&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgIrCiMKHXByb21vdGlvbl8xMDAwNTY0X3R4Yl9lbmdjb21wEAcYASIECAUILA%3D%3D:S:ANO1ljJhfZA&gsr=Ci6yAisKIwodcHJvbW90aW9uXzEwMDA1NjRfdHhiX2VuZ2NvbXAQBxgBIgQIBQgs:S:ANO1ljIRSrY&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fOEQxRjFGOTVfMkQxM0JDQkJfNDlEMUY5OTUQBxgB:S:ANO1ljLYlPE&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb184RDFGMUY5NV8yRDEzQkNCQl80OUQxRjk5NRAHGAE%3D:S:ANO1ljKmVuQ',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fOEQxRjFGOTVfMkQxM0JDQkJfNDlEMUY5OTUQBxgB:S:ANO1ljLYlPE&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb184RDFGMUY5NV8yRDEzQkNCQl80OUQxRjk5NRAHGAE%3D:S:ANO1ljKmVuQ',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fNkUwMTU5ODlfRDJFQjExRUFfOTEyQTFDMjIQBxgB:S:ANO1ljJgDKQ&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb182RTAxNTk4OV9EMkVCMTFFQV85MTJBMUMyMhAHGAE%3D:S:ANO1ljJwDJM',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fNDEyNzk5NEZfRTVGOUI3RDdfRjMzNUQ3ODYQBxgB:S:ANO1ljJSMtU&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb180MTI3OTk0Rl9FNUY5QjdEN19GMzM1RDc4NhAHGAE%3D:S:ANO1ljKKZn8',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fRjFCOTZFNTBfQTJEQzQ1MTRfNjc0MUFBQzQQBxgB:S:ANO1ljJZde4&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb19GMUI5NkU1MF9BMkRDNDUxNF82NzQxQUFDNBAHGAE%3D:S:ANO1ljJz2XU',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fRTMwOTFFM0RfOTUwMUQ1QzNfQzJBOEEzRkMQBxgB:S:ANO1ljJVSLs&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb19FMzA5MUUzRF85NTAxRDVDM19DMkE4QTNGQxAHGAE%3D:S:ANO1ljIPpVY',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fNzUxNjFFNzNfNERENDJEOEVfMTg0MjdFREYQBxgB:S:ANO1ljLeK1k&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb183NTE2MUU3M180REQ0MkQ4RV8xODQyN0VERhAHGAE%3D:S:ANO1ljJivVM',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fNDMxREUwM0VfRkIzQkM2M0ZfNzE1MEZFNDQQBxgB:S:ANO1ljKWBLY&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb180MzFERTAzRV9GQjNCQzYzRl83MTUwRkU0NBAHGAE%3D:S:ANO1ljLZd1s',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fNTYzMUREMzBfMTdFNTlFNjZfMUZFOTg4RTAQBxgB:S:ANO1ljJ3SFA&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb181NjMxREQzMF8xN0U1OUU2Nl8xRkU5ODhFMBAHGAE%3D:S:ANO1ljJZOwc',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fNUE1NTNCQkNfOTIyNjVBNUNfMjkxNkM5NzkQBxgB:S:ANO1ljLgUUo&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb181QTU1M0JCQ185MjI2NUE1Q18yOTE2Qzk3ORAHGAE%3D:S:ANO1ljLXbLI',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fNzU5NEQ3MDJfODE1RkJBNzlfQ0ZBMDZGNjkQBxgB:S:ANO1ljLwAAc&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb183NTk0RDcwMl84MTVGQkE3OV9DRkEwNkY2ORAHGAE%3D:S:ANO1ljI_Zgo',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fQzRDMkRFMUVfMkUxN0MwMEVfNjBBMTQxNEMQBxgB:S:ANO1ljLb-Fw&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb19DNEMyREUxRV8yRTE3QzAwRV82MEExNDE0QxAHGAE%3D:S:ANO1ljImkgU',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fQzRDMkRFMUVfMkUxN0MwMEVfNjBBMTQxNEMQBxgB:S:ANO1ljLb-Fw&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb19DNEMyREUxRV8yRTE3QzAwRV82MEExNDE0QxAHGAE%3D:S:ANO1ljImkgU',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fRUNDNTcxOUFfMUE1N0NDNzhfNkUwNTQ1MDkQBxgB:S:ANO1ljJXNpA&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb19FQ0M1NzE5QV8xQTU3Q0M3OF82RTA1NDUwORAHGAE%3D:S:ANO1ljL5W3o',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fN0QyNjkzQTJfOTQ0MkIwNzNfQzE1NTQ3NEEQBxgB:S:ANO1ljJZ0CQ&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb183RDI2OTNBMl85NDQyQjA3M19DMTU1NDc0QRAHGAE%3D:S:ANO1ljIUB8s',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fOUJENUM4M0NfMTY0RDZDMEZfOTI0MUQ5ODcQBxgB:S:ANO1ljKKrZc&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb185QkQ1QzgzQ18xNjRENkMwRl85MjQxRDk4NxAHGAE%3D:S:ANO1ljJmPU0',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fMTY5RjZCNTFfREM0MzE3NjZfNUVFNzdFQkMQBxgB:S:ANO1ljJSDEs&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb18xNjlGNkI1MV9EQzQzMTc2Nl81RUU3N0VCQxAHGAE%3D:S:ANO1ljLdsUs',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fRjBGQTkzNENfNEUwNkJENEVfQUZGNkUwNTIQBxgB:S:ANO1ljLXKh4&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb19GMEZBOTM0Q180RTA2QkQ0RV9BRkY2RTA1MhAHGAE%3D:S:ANO1ljIOVMo',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fQTAxNjQ1QkJfMUQ5ODYyNjJfQTY2OTI4REUQBxgB:S:ANO1ljKb7qc&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb19BMDE2NDVCQl8xRDk4NjI2Ml9BNjY5MjhERRAHGAE%3D:S:ANO1ljKfppE',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fQUVBNDZEQ0FfMEJGRTBGOUFfMkY4NTNBOEMQBxgB:S:ANO1ljK2ykM&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb19BRUE0NkRDQV8wQkZFMEY5QV8yRjg1M0E4QxAHGAE%3D:S:ANO1ljKYTm8',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fOUFGMEYyNzVfNDYzQkJENzBfMEY3NjFEQTYQBxgB:S:ANO1ljLWmpI&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb185QUYwRjI3NV80NjNCQkQ3MF8wRjc2MURBNhAHGAE%3D:S:ANO1ljKaEmk',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fNUU5NDM0MkFfNjJGOTI3NTJfRTk1RjRCMkUQBxgB:S:ANO1ljKzDzE&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb181RTk0MzQyQV82MkY5Mjc1Ml9FOTVGNEIyRRAHGAE%3D:S:ANO1ljKbT5g',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fN0MwMkJDREFfMzdENEQ1OTBfODFERTY3QjgQBxgB:S:ANO1ljK6VvM&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb183QzAyQkNEQV8zN0Q0RDU5MF84MURFNjdCOBAHGAE%3D:S:ANO1ljILU5I',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fMzIxRjUwMDNfNTA2NTU5MDVfMDJCNzBDNzEQBxgB:S:ANO1ljLmiR4&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb18zMjFGNTAwM181MDY1NTkwNV8wMkI3MEM3MRAHGAE%3D:S:ANO1ljINXoA',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fMDE4NDE1QzJfMDFDNkU2NzlfMEI0NEEwRDUQBxgB:S:ANO1ljLmUUI&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb18wMTg0MTVDMl8wMUM2RTY3OV8wQjQ0QTBENRAHGAE%3D:S:ANO1ljIjlYg',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fQTMwMkRCN0JfQzkzREJBODVfNzgyNTRGMTAQBxgB:S:ANO1ljKi4n0&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb19BMzAyREI3Ql9DOTNEQkE4NV83ODI1NEYxMBAHGAE%3D:S:ANO1ljKLAQk',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fNDBEQzY5QzdfNzExMzAyNEZfQ0NDQzgyRTQQBxgB:S:ANO1ljL22hc&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb180MERDNjlDN183MTEzMDI0Rl9DQ0NDODJFNBAHGAE%3D:S:ANO1ljKUud8',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fOTYzOEM4RjdfOUEwRTFDRTlfRDlBNzQ0OTAQBxgB:S:ANO1ljIjHLk&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb185NjM4QzhGN185QTBFMUNFOV9EOUE3NDQ5MBAHGAE%3D:S:ANO1ljK08eU',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fOEYyMzM4MzZfQTcwMTVFMTlfMTVGNzI1OTQQBxgB:S:ANO1ljIxqiM&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb184RjIzMzgzNl9BNzAxNUUxOV8xNUY3MjU5NBAHGAE%3D:S:ANO1ljIHXXE',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fRjBENTgyMEZfODM4MDg1MTBfQURGODcwNDAQBxgB:S:ANO1ljI4d2M&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb19GMEQ1ODIwRl84MzgwODUxMF9BREY4NzA0MBAHGAE%3D:S:ANO1ljI0DBk',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fQTBGNUZEREZfRTczREY2NjFfNjA5QjYyMzQQBxgB:S:ANO1ljI1G18&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb19BMEY1RkRERl9FNzNERjY2MV82MDlCNjIzNBAHGAE%3D:S:ANO1ljJCSf0',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fODIwRDg2RDRfNEZGRTdCMzFfNEY1QTJEQjAQBxgB:S:ANO1ljIRMks&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb184MjBEODZENF80RkZFN0IzMV80RjVBMkRCMBAHGAE%3D:S:ANO1ljIIYdc',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fRERDNDIzQjZfNzNGM0U0ODdfQkYwNUJFNTQQBxgB:S:ANO1ljKayqI&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb19EREM0MjNCNl83M0YzRTQ4N19CRjA1QkU1NBAHGAE%3D:S:ANO1ljJG-9w',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fMkI4NTBCQTJfMzNCM0UzOThfMzc2MzQ3MDgQBxgB:S:ANO1ljJKpeg&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb18yQjg1MEJBMl8zM0IzRTM5OF8zNzYzNDcwOBAHGAE%3D:S:ANO1ljJxJL0',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fMjg1QkMwRjVfRkMwMDIwMUNfQzhDNkYzNjEQBxgB:S:ANO1ljIFnX8&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb18yODVCQzBGNV9GQzAwMjAxQ19DOEM2RjM2MRAHGAE%3D:S:ANO1ljK1oW8',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fMzIxOTY4RERfNkY2MUE4OTVfOTg1QzQzQzkQBxgB:S:ANO1ljIYX3U&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb18zMjE5NjhERF82RjYxQTg5NV85ODVDNDNDORAHGAE%3D:S:ANO1ljK6SXc',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fOTdGRTdCQTVfRkZDNTM0RjhfODBCRjAyMDQQBxgB:S:ANO1ljJGLvs&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb185N0ZFN0JBNV9GRkM1MzRGOF84MEJGMDIwNBAHGAE%3D:S:ANO1ljKw2V8',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fQ0NENTVBQkZfMTcwRjlEMDVfNkMyRDM0OTkQBxgB:S:ANO1ljKarSA&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb19DQ0Q1NUFCRl8xNzBGOUQwNV82QzJEMzQ5ORAHGAE%3D:S:ANO1ljIgLK4',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fMTZDQjk5MDFfMzNDNzAxMkVfNjNBNTU4QUEQBxgB:S:ANO1ljIqCwU&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb18xNkNCOTkwMV8zM0M3MDEyRV82M0E1NThBQRAHGAE%3D:S:ANO1ljI7J88',
    'https://play.google.com/store/books/collection/cluster?clp=CjcKNQovYm9va3NfY2x1c3RlcnNfbXJsX29fNkI3RkJFNDdfMjY3MUQyRDFfQzBBREI2NkQQBxgB:S:ANO1ljLKYdc&gsr=CjkKNwo1Ci9ib29rc19jbHVzdGVyc19tcmxfb182QjdGQkU0N18yNjcxRDJEMV9DMEFEQjY2RBAHGAE%3D:S:ANO1ljI3rso',
    'https://play.google.com/store/books/collection/cluster?clp=sgIxCikKI3Byb21vdGlvbl8xMDAyMDMwX2Jpb19keW5hbWljX3dvbWVuEAcYASIECAUILA%3D%3D:S:ANO1ljIoSiQ&gsr=CjSyAjEKKQojcHJvbW90aW9uXzEwMDIwMzBfYmlvX2R5bmFtaWNfd29tZW4QBxgBIgQIBQgs:S:ANO1ljIRd3c&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgI2Ci4KKHByb21vdGlvbl8xMDAyMDI0X2Jpb19keW5hbWljX2hpc3RvcmljYWwQBxgBIgQIBQgs:S:ANO1ljIuyxI&gsr=CjmyAjYKLgoocHJvbW90aW9uXzEwMDIwMjRfYmlvX2R5bmFtaWNfaGlzdG9yaWNhbBAHGAEiBAgFCCw%3D:S:ANO1ljIs2d8&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgI3Ci8KKXByb21vdGlvbl8xMDAyMDI1X2Jpb19keW5hbWljX3NjaWVuY2V0ZWNoEAcYASIECAUILA%3D%3D:S:ANO1ljKcva8&gsr=CjqyAjcKLwopcHJvbW90aW9uXzEwMDIwMjVfYmlvX2R5bmFtaWNfc2NpZW5jZXRlY2gQBxgBIgQIBQgs:S:ANO1ljLsTY0&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgI1Ci0KJ3Byb21vdGlvbl8xMDAyMDIyX2Jpb19keW5hbWljX2NyaW1pbmFscxAHGAEiBAgFCCw%3D:S:ANO1ljKXV3Q&gsr=CjiyAjUKLQoncHJvbW90aW9uXzEwMDIwMjJfYmlvX2R5bmFtaWNfY3JpbWluYWxzEAcYASIECAUILA%3D%3D:S:ANO1ljJZqXg&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgI7CjMKLXByb21vdGlvbl8xMDAyMDMxX2Jpb19keW5hbWljX3BlcnNvbmFsbWVtb2lycxAHGAEiBAgFCCw%3D:S:ANO1ljJS2Pg&gsr=Cj6yAjsKMwotcHJvbW90aW9uXzEwMDIwMzFfYmlvX2R5bmFtaWNfcGVyc29uYWxtZW1vaXJzEAcYASIECAUILA%3D%3D:S:ANO1ljIQLTs&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgI3Ci8KKXByb21vdGlvbl8xMDAyMDFmX2Jpb19keW5hbWljX2FkdmVudHVyZXJzEAcYASIECAUILA%3D%3D:S:ANO1ljJ3DDM&gsr=CjqyAjcKLwopcHJvbW90aW9uXzEwMDIwMWZfYmlvX2R5bmFtaWNfYWR2ZW50dXJlcnMQBxgBIgQIBQgs:S:ANO1ljIDJ0E&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=ogQcCAgSFGF1ZGlvYm9va3NfY29sbF8xMjIyGgIIQA%3D%3D:S:ANO1ljKOmmQ&gsr=Ch-iBBwICBIUYXVkaW9ib29rc19jb2xsXzEyMjIaAghA:S:ANO1ljKjC-s&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=ogQcCAgSFGF1ZGlvYm9va3NfY29sbF8xMjI0GgIIQA%3D%3D:S:ANO1ljLDR98&gsr=Ch-iBBwICBIUYXVkaW9ib29rc19jb2xsXzEyMjQaAghA:S:ANO1ljKZ-PE&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgItCiUKH3Byb21vdGlvbl8xMDAxNDBmX25ld19teXN0ZXJpZXMQBxgBIgQIBQgs:S:ANO1ljKj2bM&gsr=CjCyAi0KJQofcHJvbW90aW9uXzEwMDE0MGZfbmV3X215c3RlcmllcxAHGAEiBAgFCCw%3D:S:ANO1ljJBqdk&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgIxCikKI3Byb21vdGlvbl8xMDAxNDEwX3BvcHVsYXJfbXlzdGVyaWVzEAcYASIECAUILA%3D%3D:S:ANO1ljKTp4k&gsr=CjSyAjEKKQojcHJvbW90aW9uXzEwMDE0MTBfcG9wdWxhcl9teXN0ZXJpZXMQBxgBIgQIBQgs:S:ANO1ljKoMmw&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgI3Ci8KKXByb21vdGlvbl8xMDAyNjIzX2VkZ2FyX2F3YXJkc19teXN0ZXJ5X21sEAcYASIECAUILA%3D%3D:S:ANO1ljJb9GA&gsr=CjqyAjcKLwopcHJvbW90aW9uXzEwMDI2MjNfZWRnYXJfYXdhcmRzX215c3RlcnlfbWwQBxgBIgQIBQgs:S:ANO1ljIjGNM&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgI7CjMKLXByb21vdGlvbl8xMDAwYzhmX215c3RlcnlfdGhyaWxsZXJfZXNzZW50aWFscxAHGAEiBAgFCCw%3D:S:ANO1ljJ81X0&gsr=Cj6yAjsKMwotcHJvbW90aW9uXzEwMDBjOGZfbXlzdGVyeV90aHJpbGxlcl9lc3NlbnRpYWxzEAcYASIECAUILA%3D%3D:S:ANO1ljIZjew&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgJECjwKNnByb21vdGlvbl8xMDAxZmZhX215c3Rlcnl0aHJpbGxlcl9keW5hbWljX3dvbWVuc2xldXRocxAHGAEiBAgFCCw%3D:S:ANO1ljJCud0&gsr=CkeyAkQKPAo2cHJvbW90aW9uXzEwMDFmZmFfbXlzdGVyeXRocmlsbGVyX2R5bmFtaWNfd29tZW5zbGV1dGhzEAcYASIECAUILA%3D%3D:S:ANO1ljJhUtU&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgIzCisKJXByb21vdGlvbl8xMDAyMjZhX3BhdHRlcnNvbl9ib29rc2hvdHMQBxgBIgQIBQgs:S:ANO1ljJhoz4&gsr=CjayAjMKKwolcHJvbW90aW9uXzEwMDIyNmFfcGF0dGVyc29uX2Jvb2tzaG90cxAHGAEiBAgFCCw%3D:S:ANO1ljLwwr8&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgIuCiYKIHByb21vdGlvbl8xMDAxNDExX2NvenlfbXlzdGVyaWVzEAcYASIECAUILA%3D%3D:S:ANO1ljITkOM&gsr=CjGyAi4KJgogcHJvbW90aW9uXzEwMDE0MTFfY296eV9teXN0ZXJpZXMQBxgBIgQIBQgs:S:ANO1ljK9A6Q&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgJICkAKOnByb21vdGlvbl8xMDAxZmYzX215c3Rlcnl0aHJpbGxlcl9keW5hbWljX3BvbGljZXByb2NlZHVyYWwQBxgBIgQIBQgs:S:ANO1ljKKnkw&gsr=CkuyAkgKQAo6cHJvbW90aW9uXzEwMDFmZjNfbXlzdGVyeXRocmlsbGVyX2R5bmFtaWNfcG9saWNlcHJvY2VkdXJhbBAHGAEiBAgFCCw%3D:S:ANO1ljJ4azM&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgJCCjoKNHByb21vdGlvbl8xMDAxZmVmX215c3Rlcnl0aHJpbGxlcl9keW5hbWljX2hhcmRib2lsZWQQBxgBIgQIBQgs:S:ANO1ljKjviM&gsr=CkWyAkIKOgo0cHJvbW90aW9uXzEwMDFmZWZfbXlzdGVyeXRocmlsbGVyX2R5bmFtaWNfaGFyZGJvaWxlZBAHGAEiBAgFCCw%3D:S:ANO1ljJ9OlE&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgJBCjkKM3Byb21vdGlvbl8xMDAxZmY4X215c3Rlcnl0aHJpbGxlcl9keW5hbWljX3RydWVjcmltZRAHGAEiBAgFCCw%3D:S:ANO1ljJJ48U&gsr=CkSyAkEKOQozcHJvbW90aW9uXzEwMDFmZjhfbXlzdGVyeXRocmlsbGVyX2R5bmFtaWNfdHJ1ZWNyaW1lEAcYASIECAUILA%3D%3D:S:ANO1ljIAGx0&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgI0CiwKJnByb21vdGlvbl8xMDAxNDBlX3BhcmFub3JtYWxfbXlzdGVyaWVzEAcYASIECAUILA%3D%3D:S:ANO1ljIsGK4&gsr=CjeyAjQKLAomcHJvbW90aW9uXzEwMDE0MGVfcGFyYW5vcm1hbF9teXN0ZXJpZXMQBxgBIgQIBQgs:S:ANO1ljLfyj4&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgJCCjoKNHByb21vdGlvbl8xMDAxZmYwX215c3Rlcnl0aHJpbGxlcl9keW5hbWljX2hpc3RvcmljYWwQBxgBIgQIBQgs:S:ANO1ljIDZYM&gsr=CkWyAkIKOgo0cHJvbW90aW9uXzEwMDFmZjBfbXlzdGVyeXRocmlsbGVyX2R5bmFtaWNfaGlzdG9yaWNhbBAHGAEiBAgFCCw%3D:S:ANO1ljI3aQQ&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgJACjgKMnByb21vdGlvbl8xMDAxZmY0X215c3Rlcnl0aHJpbGxlcl9keW5hbWljX3N1c3BlbnNlEAcYASIECAUILA%3D%3D:S:ANO1ljKmMyU&gsr=CkOyAkAKOAoycHJvbW90aW9uXzEwMDFmZjRfbXlzdGVyeXRocmlsbGVyX2R5bmFtaWNfc3VzcGVuc2UQBxgBIgQIBQgs:S:ANO1ljIArdc&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgJKCkIKPHByb21vdGlvbl8xMDAxZmY3X215c3Rlcnl0aHJpbGxlcl9keW5hbWljX3RyYWRpdGlvbmFsYnJpdGlzaBAHGAEiBAgFCCw%3D:S:ANO1ljIUnYQ&gsr=Ck2yAkoKQgo8cHJvbW90aW9uXzEwMDFmZjdfbXlzdGVyeXRocmlsbGVyX2R5bmFtaWNfdHJhZGl0aW9uYWxicml0aXNoEAcYASIECAUILA%3D%3D:S:ANO1ljJHquM&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgIxCikKI3Byb21vdGlvbl8xMDAxNDBkX3NwYW5pc2hfbXlzdGVyaWVzEAcYASIECAUILA%3D%3D:S:ANO1ljJB2dA&gsr=CjSyAjEKKQojcHJvbW90aW9uXzEwMDE0MGRfc3BhbmlzaF9teXN0ZXJpZXMQBxgBIgQIBQgs:S:ANO1ljJQ7oA&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgInCh8KGXByb21vdGlvbl9mYXJtX3RvX3RhYmxlXzEQBxgBIgQIBQgs:S:ANO1ljKqpUk&gsr=CiqyAicKHwoZcHJvbW90aW9uX2Zhcm1fdG9fdGFibGVfMRAHGAEiBAgFCCw%3D:S:ANO1ljLKSaI&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgIzCisKJXByb21vdGlvbl9pdF9zX2Fsd2F5c19jb2NrdGFpbF9ob3VyXzEQBxgBIgQIBQgs:S:ANO1ljI0ZTA&gsr=CjayAjMKKwolcHJvbW90aW9uX2l0X3NfYWx3YXlzX2NvY2t0YWlsX2hvdXJfMRAHGAEiBAgFCCw%3D:S:ANO1ljLc1Bg&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgInCh8KGXByb21vdGlvbl9pbmRvb3JfZ2FyZGVuXzEQBxgBIgQIBQgs:S:ANO1ljKgNnQ&gsr=CiqyAicKHwoZcHJvbW90aW9uX2luZG9vcl9nYXJkZW5fMRAHGAEiBAgFCCw%3D:S:ANO1ljKjPC4&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgIwCigKInByb21vdGlvbl95b3VyX2Jlc3RfZGlubmVyX3BhcnR5XzEQBxgBIgQIBQgs:S:ANO1ljKsj2o&gsr=CjOyAjAKKAoicHJvbW90aW9uX3lvdXJfYmVzdF9kaW5uZXJfcGFydHlfMRAHGAEiBAgFCCw%3D:S:ANO1ljIrKzc&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgIqCiIKHHByb21vdGlvbl90b3BfYm9va3NfaW5fZGl5XzEQBxgBIgQIBQgs:S:ANO1ljKHFvk&gsr=Ci2yAioKIgoccHJvbW90aW9uX3RvcF9ib29rc19pbl9kaXlfMRAHGAEiBAgFCCw%3D:S:ANO1ljJ9CmY&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgIrCiMKHXByb21vdGlvbl90aGVfZ3JlYXRfaW5kb29yc18xEAcYASIECAUILA%3D%3D:S:ANO1ljKmTzQ&gsr=Ci6yAisKIwodcHJvbW90aW9uX3RoZV9ncmVhdF9pbmRvb3JzXzEQBxgBIgQIBQgs:S:ANO1ljL5pAA&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgIoCiAKGnByb21vdGlvbl9vcmdhbmljX2xpdmluZ18xEAcYASIECAUILA%3D%3D:S:ANO1ljK7Pbw&gsr=CiuyAigKIAoacHJvbW90aW9uX29yZ2FuaWNfbGl2aW5nXzEQBxgBIgQIBQgs:S:ANO1ljKzLzs&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgIlCh0KF3Byb21vdGlvbl9ncmVlbl90aHVtYl8xEAcYASIECAUILA%3D%3D:S:ANO1ljKWdaI&gsr=CiiyAiUKHQoXcHJvbW90aW9uX2dyZWVuX3RodW1iXzEQBxgBIgQIBQgs:S:ANO1ljJdBf8&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgItCiUKH3Byb21vdGlvbl9jYW5fcGlja2xlX3ByZXNlcnZlXzEQBxgBIgQIBQgs:S:ANO1ljLc1QY&gsr=CjCyAi0KJQofcHJvbW90aW9uX2Nhbl9waWNrbGVfcHJlc2VydmVfMRAHGAEiBAgFCCw%3D:S:ANO1ljIR0Es&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgIpCiEKG3Byb21vdGlvbl9kcmlua3NfZHJpbmtpbmdfMRAHGAEiBAgFCCw%3D:S:ANO1ljILKm0&gsr=CiyyAikKIQobcHJvbW90aW9uX2RyaW5rc19kcmlua2luZ18xEAcYASIECAUILA%3D%3D:S:ANO1ljKp87k&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgIoCiAKGnByb21vdGlvbl9mbG93ZXJzX2FfdG9fel8xEAcYASIECAUILA%3D%3D:S:ANO1ljKqkMQ&gsr=CiuyAigKIAoacHJvbW90aW9uX2Zsb3dlcnNfYV90b196XzEQBxgBIgQIBQgs:S:ANO1ljJd77A&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgIoCiAKGnByb21vdGlvbl9uYXR1cmVfd3JpdGluZ18xEAcYASIECAUILA%3D%3D:S:ANO1ljJVNIk&gsr=CiuyAigKIAoacHJvbW90aW9uX25hdHVyZV93cml0aW5nXzEQBxgBIgQIBQgs:S:ANO1ljIDdXk&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgIkChwKFnByb21vdGlvbl9wYXJ0eV90aW1lXzEQBxgBIgQIBQgs:S:ANO1ljJkl0I&gsr=CieyAiQKHAoWcHJvbW90aW9uX3BhcnR5X3RpbWVfMRAHGAEiBAgFCCw%3D:S:ANO1ljJz098&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgJECjwKNnByb21vdGlvbl8xMDAyYTU1X2Vib29rc19mcmVlX2ZpcnN0c192YWxlbnRpbmVzZGF5MjAxOBBEGAEiBAgFCCw%3D:S:ANO1ljKVuUY&gsr=CkeyAkQKPAo2cHJvbW90aW9uXzEwMDJhNTVfZWJvb2tzX2ZyZWVfZmlyc3RzX3ZhbGVudGluZXNkYXkyMDE4EEQYASIECAUILA%3D%3D:S:ANO1ljLQ26s&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgI3Ci8KKXByb21vdGlvbl8xMDAyMzhlX2tlbnNpbmd0b25fcm9tYW5jZV9zYWxlEEQYASIECAUILA%3D%3D:S:ANO1ljJTXqo&gsr=CjqyAjcKLwopcHJvbW90aW9uXzEwMDIzOGVfa2Vuc2luZ3Rvbl9yb21hbmNlX3NhbGUQRBgBIgQIBQgs:S:ANO1ljJcEUM&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgI3Ci8KKXByb21vdGlvbl8xMDAxZmUyX3JvbWFuY2Vfd2VzdGVybl9keW5hbWljEEQYASIECAUILA%3D%3D:S:ANO1ljJd57s&gsr=CjqyAjcKLwopcHJvbW90aW9uXzEwMDFmZTJfcm9tYW5jZV93ZXN0ZXJuX2R5bmFtaWMQRBgBIgQIBQgs:S:ANO1ljIhn0w&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgI4CjAKKnByb21vdGlvbl8xMDAxZmUwX3JvbWFuY2Vfc3VzcGVuc2VfZHluYW1pYxBEGAEiBAgFCCw%3D:S:ANO1ljKF_gM&gsr=CjuyAjgKMAoqcHJvbW90aW9uXzEwMDFmZTBfcm9tYW5jZV9zdXNwZW5zZV9keW5hbWljEEQYASIECAUILA%3D%3D:S:ANO1ljIy_Fo&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgI3Ci8KKXByb21vdGlvbl8xMDAxZmRjX3JvbWFuY2VfZmFudGFzeV9keW5hbWljEEQYASIECAUILA%3D%3D:S:ANO1ljIYSLY&gsr=CjqyAjcKLwopcHJvbW90aW9uXzEwMDFmZGNfcm9tYW5jZV9mYW50YXN5X2R5bmFtaWMQRBgBIgQIBQgs:S:ANO1ljKZPDc&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgI6CjIKLHByb21vdGlvbl8xMDAxZmRmX3JvbWFuY2VfcGFyYW5vcm1hbF9keW5hbWljEEQYASIECAUILA%3D%3D:S:ANO1ljKSxpY&gsr=Cj2yAjoKMgoscHJvbW90aW9uXzEwMDFmZGZfcm9tYW5jZV9wYXJhbm9ybWFsX2R5bmFtaWMQRBgBIgQIBQgs:S:ANO1ljKYsMQ&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgItCiUKH3Byb21vdGlvbl8xMDAwZjE4X3dvcmxkX3dhcl9vbmUQBxgBIgQIBQgs:S:ANO1ljIJT-o&gsr=CjCyAi0KJQofcHJvbW90aW9uXzEwMDBmMThfd29ybGRfd2FyX29uZRAHGAEiBAgFCCw%3D:S:ANO1ljIFKSg&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgI4CjAKKnByb21vdGlvbl8xMDAyMWVjX2hpc3RvcnlfbWVkaWV2YWxfZHluYW1pYxAHGAEiBAgFCCw%3D:S:ANO1ljIEkrg&gsr=CjuyAjgKMAoqcHJvbW90aW9uXzEwMDIxZWNfaGlzdG9yeV9tZWRpZXZhbF9keW5hbWljEAcYASIECAUILA%3D%3D:S:ANO1ljItCCU&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgIsCiQKHnByb21vdGlvbl8xMDAwZjFkX2Jpb19tZW1vcmllcxAHGAEiBAgFCCw%3D:S:ANO1ljIOLcs&gsr=Ci-yAiwKJAoecHJvbW90aW9uXzEwMDBmMWRfYmlvX21lbW9yaWVzEAcYASIECAUILA%3D%3D:S:ANO1ljJiSvs&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgI1Ci0KJ3Byb21vdGlvbl8xMDAyMWVhX2hpc3Rvcnlfd29ybGRfZHluYW1pYxAHGAEiBAgFCCw%3D:S:ANO1ljLJmFE&gsr=CjiyAjUKLQoncHJvbW90aW9uXzEwMDIxZWFfaGlzdG9yeV93b3JsZF9keW5hbWljEAcYASIECAUILA%3D%3D:S:ANO1ljK7x6I&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgI6CjIKLHByb21vdGlvbl8xMDAyMWViX2hpc3RvcnlfbWlkZGxlZWFzdF9keW5hbWljEAcYASIECAUILA%3D%3D:S:ANO1ljKV45c&gsr=Cj2yAjoKMgoscHJvbW90aW9uXzEwMDIxZWJfaGlzdG9yeV9taWRkbGVlYXN0X2R5bmFtaWMQBxgBIgQIBQgs:S:ANO1ljLh-JM&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgI0CiwKJnByb21vdGlvbl8xMDAyMWU4X2hpc3RvcnlfV1dJSV9keW5hbWljEAcYASIECAUILA%3D%3D:S:ANO1ljIHc1I&gsr=CjeyAjQKLAomcHJvbW90aW9uXzEwMDIxZThfaGlzdG9yeV9XV0lJX2R5bmFtaWMQBxgBIgQIBQgs:S:ANO1ljJIe1Q&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgI4CjAKKnByb21vdGlvbl8xMDAyMWU5X2hpc3RvcnlfY2l2aWx3YXJfZHluYW1pYxAHGAEiBAgFCCw%3D:S:ANO1ljL2--E&gsr=CjuyAjgKMAoqcHJvbW90aW9uXzEwMDIxZTlfaGlzdG9yeV9jaXZpbHdhcl9keW5hbWljEAcYASIECAUILA%3D%3D:S:ANO1ljJbFJY&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgI_CjcKMXByb21vdGlvbl8xMDAyMWU2X2hpc3RvcnlfYWZyaWNhbmFtZXJpY2FuX2R5bmFtaWMQBxgBIgQIBQgs:S:ANO1ljII9rg&gsr=CkKyAj8KNwoxcHJvbW90aW9uXzEwMDIxZTZfaGlzdG9yeV9hZnJpY2FuYW1lcmljYW5fZHluYW1pYxAHGAEiBAgFCCw%3D:S:ANO1ljKXk8g&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgIwCigKInByb21vdGlvbl8xMDAwZjE3X21pbGl0YXJ5X2hpc3RvcnkQBxgBIgQIBQgs:S:ANO1ljKfwik&gsr=CjOyAjAKKAoicHJvbW90aW9uXzEwMDBmMTdfbWlsaXRhcnlfaGlzdG9yeRAHGAEiBAgFCCw%3D:S:ANO1ljKqWkE&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgIyCioKJHByb21vdGlvbl8xMDAwZjJiX2hpc3RvcmljYWxfZmljdGlvbhAHGAEiBAgFCCw%3D:S:ANO1ljJpOAA&gsr=CjWyAjIKKgokcHJvbW90aW9uXzEwMDBmMmJfaGlzdG9yaWNhbF9maWN0aW9uEAcYASIECAUILA%3D%3D:S:ANO1ljI5BHI&hl=en&gl=US',
    'https://play.google.com/store/books/collection/cluster?clp=sgIuCiYKIHByb21vdGlvbl8xMDAwZjJjX3dvbWVuc19oaXN0b3J5EAcYASIECAUILA%3D%3D:S:ANO1ljIBMEM&gsr=CjGyAi4KJgogcHJvbW90aW9uXzEwMDBmMmNfd29tZW5zX2hpc3RvcnkQBxgBIgQIBQgs:S:ANO1ljJNgn0&hl=en&gl=US',
]

headers = "id,isbn,title,description,author,genre,language,image\n"
f = open('test4.csv','w')
f.write(headers)
f.close()

for url in dict:
     extract(url,'test4.csv')

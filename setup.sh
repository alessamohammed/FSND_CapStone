#!/bin/bash
export AUTH0_DOMAIN='dev-g-z09scw.us.auth0.com'
export ALGORITHMS=['RS256']
export API_AUDIENCE='Casting'
export DATABASE_URL='postgresql://cap:1122@localhost:5432/casting'
export CLIENT_ID='Rz6YyS9V9I8ghwu3fY0ark7zACP5CHNQ'
export CLIENT_SECRET='b1RsxHultg5EEcnfMF1YCLZnKNDl2nO9Cii7847iI31Bw6YgVRJFa9QZnk5-ODOc'
export EXECUTIVE='bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtId3kxVnR1cHpYNWtFY2R2SC10YiJ9.eyJpc3MiOiJodHRwczovL2Rldi1nLXowOXNjdy51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDc5ODY2NjI1MTgxOTkwMzEyMzAiLCJhdWQiOiJDYXN0aW5nIiwiaWF0IjoxNjMzOTMxNDIxLCJleHAiOjE2MzM5Mzk0MjEsImF6cCI6IlJ6Nll5UzlWOUk4Z2h3dTNmWTBhcms3ekFDUDVDSE5RIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwibW9kaWZ5OmFjdG9ycyIsIm1vZGlmeTptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.jo6xnj5Sw42pLgfrviLmiTcAecVYfRRh6NizyIHEz-tLfh0WqKtAwQGLB83tQsNbUFwq8Lubg61lcsRPYEGwotiQJ5wTp2kR02WOd_YkMsPfJVtVF9FVo8P4kxXla77NgQdVohgHT11Ghk6iyzgOMOCpL5rMWaO4S_b4NhtlBbYxyZtvjlqnpYHU-qcuSPlqtiQ6V17DqDUsSDBODjzMKXAu0NnmzHEVaWCOxfRQpnJ1AiPlqjMbZghNKnZr4JBPVEIxb2FFvwzPg7rf_DXd5f9COD3eKSPX_EOgb8N2XOG3C1yNsAQI6wIoUZHyup-UkiaGQ-KmIRZBhszcRaLE_A'
export DIRECTOR='bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtId3kxVnR1cHpYNWtFY2R2SC10YiJ9.eyJpc3MiOiJodHRwczovL2Rldi1nLXowOXNjdy51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTUyNjY2MjMxNDM3MTI3MTk2NzgiLCJhdWQiOiJDYXN0aW5nIiwiaWF0IjoxNjMzOTMxODEzLCJleHAiOjE2MzM5Mzk4MTMsImF6cCI6IlJ6Nll5UzlWOUk4Z2h3dTNmWTBhcms3ekFDUDVDSE5RIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJtb2RpZnk6YWN0b3JzIiwibW9kaWZ5Om1vdmllcyIsInBvc3Q6YWN0b3JzIl19.B-Jb-KQVr4LmzdUGTge68v33c85_xvVqt28yxTBuI94Wvs_uGROmCS81shMtaPtI_LN9B57w9fN1omysMTkfy3MuYozYk_h_RFKVxxXUylv5meXn2nKPB7ZhSyVHFAlNO0BU9-fnzZkZE_uAwdkrnhQ7VWMnLc0_p6hLuqMdwoV0DJkiGNFSv8AVOUeOw0K5RGZSFmYDZvzYGDkpzReA1VYZBAKP83D2AH8ksPHNGF3vY5aL-9EsoeH2mZ4C9KYkvIRpSPEzRT0rmVXmsDi28SUiewcGOfWPXnaD4E-eZy5MJEgnw-t56hP-hAchOSSfsFVx1Xy7WKdqnBTpord0oQ'
export ASSISTANT='bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtId3kxVnR1cHpYNWtFY2R2SC10YiJ9.eyJpc3MiOiJodHRwczovL2Rldi1nLXowOXNjdy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE2MjZmOWEwNjcyMWUwMDY5MGJiZjBkIiwiYXVkIjoiQ2FzdGluZyIsImlhdCI6MTYzMzkzMTkyOSwiZXhwIjoxNjMzOTM5OTI5LCJhenAiOiJSejZZeVM5VjlJOGdod3UzZlkwYXJrN3pBQ1A1Q0hOUSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.2ojrA5nYBWEfTCeofsHRdbpl5KMz7GwnWU_UIevAMkVzvIcHiEfMcElkrVHGby1_k3pn4wUqPte-cUir-w45_thh6cckK4engiiR1Spc8Jz5vInpx2tQXHSknOpWVDPeMHeaq66mCNCgxEZp9g10oyRDczWulPlX_UQCG5uKjjFWS5TyK-w-QPO_-tnZ8VPT1xgu2tjH-3G40ZPWEtdz8RWzB7qwtU4H7AqZ6vKc-PANbWHxbBXV09RTowFpQX94fFp3jSG80ICPmufNOI8p0tVnDdMblfj3pyC_Y7gAGnXIG401Oa1T4mF_9SEb8wq59oN2lQ5WF6mJxqqOlZNxDA'
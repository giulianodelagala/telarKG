# Some MilleniumDB routines
import subprocess
import os
import signal


class ML:
    def __init__(self, port=8080) -> None:
        # Assume that the script is run from the root directory
        # WORKING_DIR = os.getcwd()
        self.WORKING_DIR = "~/MDB-Compatibilidad/MillenniumDB-Dev"
        # Executables paths
        self.EXECUTABLES_DIR = os.path.join(self.WORKING_DIR, "build/Release/bin")
        self.CREATE_DB_EXECUTABLE = os.path.join(
            self.EXECUTABLES_DIR, "create_db_sparql"
        )
        self.SERVER_EXECUTABLE = os.path.join(self.EXECUTABLES_DIR, "server")
        self.QUERY_EXECUTABLE = os.path.join(self.EXECUTABLES_DIR, "query")
        # Base
        self.TESTING_ROOT_DIR = "~/telarKG/db-compat2"
        # TESTING_SPARQL_DIR = os.path.join(TESTING_ROOT_DIR, "testing/sparql")
        # TESTING_DBS_DIR = os.path.join(TESTING_ROOT_DIR, "testing_dbs/sparql")
        self.DEFAULT_BUFFER = 100000
        self.SERVER_PORT = port

        print(self.EXECUTABLES_DIR)
        # start server n caught pid
        self.pid = self.start_server().pid

    def start_server(self):
        server_process = subprocess.Popen(
            [
                f"{self.SERVER_EXECUTABLE} {self.TESTING_ROOT_DIR} \
                 -p {self.SERVER_PORT} -b {self.DEFAULT_BUFFER}"
            ],
            shell=True,
            preexec_fn=os.setsid,
        )
        return server_process

    def run_to_file(
        self,
        test_file: str,
        output_file: str,
    ):
        with open(output_file, "w") as file:
            query_execution = subprocess.Popen(
                [
                    f"{self.QUERY_EXECUTABLE} < {test_file} -p {self.SERVER_PORT}",
                ],
                shell=True,
                stdout=file,
                stderr=subprocess.DEVNULL,
            )
            query_execution.wait()

    def run(self, query_path: str, query_file: str, port: int) -> str:
        # Run a query and take the time
        query_execution = subprocess.Popen(
            [
                f"{self.QUERY_EXECUTABLE} < {query_file} -p {self.SERVER_PORT}",
            ],
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        query_execution.wait()

        out, err = query_execution.communicate()
        result = out.decode("utf-8")

        return result

    def get_query(self, query_path: str, query_file: str) -> str:
        try:
            output = self.run(
                "",
                query_file,
                8080,
            )
            # os.killpg(telar_server.pid, signal.SIGINT)
            return output

        except Exception as error:
            os.killpg(self.pid, signal.SIGINT)
            return "Error: " + str(error)

    def shutting_down(self):
        # shutting down the server
        os.killpg(self.pid, signal.SIGINT)
        print("server shutdown")

    def __del__(self):
        self.shutting_down()

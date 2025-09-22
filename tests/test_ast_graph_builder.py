import os
import tempfile
from modules import ast_graph_builder


def test_collect_py_files_creates_relative_paths():
    with tempfile.TemporaryDirectory() as tempdir:
        file_path = os.path.join(tempdir, "test1.py")
        with open(file_path, "w") as f:
            f.write("# test file")
        result = ast_graph_builder.collect_py_files(tempdir)
        assert "test1.py" in result


def test_write_dot_file_creates_valid_output():
    with tempfile.TemporaryDirectory() as tempdir:
        dot_file = os.path.join(tempdir, "output.dot")
        py_files = {"example1.py", "dir/example2.py"}
        ast_graph_builder.write_dot_file(py_files, dot_file)

        with open(dot_file, "r", encoding="utf-8") as f:
            content = f.read()
            assert "digraph G" in content
            assert "example1.py" in content
            assert "example2.py" in content


def test_build_dependency_graph_writes_dot_file():
    with tempfile.TemporaryDirectory() as tempdir:
        os.mkdir(os.path.join(tempdir, "sub"))
        with open(os.path.join(tempdir, "sub", "file.py"), "w") as f:
            f.write("# test file")

        dot_file = os.path.join(tempdir, "output.dot")
        ast_graph_builder.build_dependency_graph(tempdir, dot_file)

        assert os.path.exists(dot_file)
        with open(dot_file, "r") as f:
            content = f.read()
            assert "file.py" in content

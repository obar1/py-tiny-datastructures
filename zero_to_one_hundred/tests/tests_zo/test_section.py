import os

from pyfakefs.fake_filesystem_unittest import Patcher

from zero_to_one_hundred.src.zero_to_one_hundred.models.section import Section
from zero_to_one_hundred.tests.conftest import str_relaxed


def test_init(get_config_map, persist_fs, process_fs, http_url_1):
    actual = Section(get_config_map, persist_fs, process_fs, http_url_1)
    assert actual.http_url == "https://cloud.google.com/abc"
    assert actual.dir_name == "https§§§cloud.google.com§abc"
    assert (
        actual.dir_readme_md
        == get_config_map.get_repo_path + "/" + "https§§§cloud.google.com§abc/readme.md"
    )
    res = actual.get_readme_md_time()
    assert res is not None


def test_write(get_config_map, persist_fs, process_fs, http_url_1):
    actual = Section(get_config_map, persist_fs, process_fs, http_url_1)
    txt = get_config_map.get_repo_path + r"/" + actual.dir_name
    txt = os.path.abspath(txt)
    with Patcher(allow_root_user=False) as patcher:
        res = actual.write(txt)
        assert res is True
        assert os.path.exists(txt)


def test_build_from_dir(get_config_map, persist_fs, process_fs):
    def simple_http():
        return "https://cloud.google.com/docs/<>:?*"

    def simple_dir():
        return "https§§§cloud.google.com§docs§§§§§§"

    assert (
        Section.build_from_dir(
            persist_fs, process_fs, get_config_map, simple_http()
        ).dir_name
        == simple_dir()
    )


def test_section_is_quest(get_gcp_config_map, persist_fs, process_fs):
    http_url = "https://www.cloudskillsboost.google/quests/257"
    actual = Section(get_gcp_config_map, persist_fs, process_fs, http_url)
    assert actual.is_gcp_quest


def test_section_is_lab(get_gcp_config_map, persist_fs, process_fs):
    http_url = "https://www.cloudskillsboost.google/course_sessions/3062553/labs"
    actual = Section(get_gcp_config_map, persist_fs, process_fs, http_url)
    assert actual.is_gcp_lab


def test_section_is_template(get_gcp_config_map, persist_fs, process_fs):
    http_url = "https://www.cloudskillsboost.google/course_templates/536"
    actual = Section(get_gcp_config_map, persist_fs, process_fs, http_url)
    assert actual.is_gcp_template


def test_section_is_gamee(get_gcp_config_map, persist_fs, process_fs):
    http_url = "https://www.cloudskillsboost.google/games/4423"
    actual = Section(get_gcp_config_map, persist_fs, process_fs, http_url)
    assert actual.is_gcp_game


def test_is_datacamp_project(get_datacamp_config_map, persist_fs, process_fs):
    http_url = "https://app.datacamp.com/learn/projects/1833"
    actual = Section(get_datacamp_config_map, persist_fs, process_fs, http_url)
    assert actual.is_datacamp_project


def test_is_datacamp_tutorial(get_datacamp_config_map, persist_fs, process_fs):
    http_url = "https://app.datacamp.com/learn/tutorials/git-push-pull"
    actual = Section(get_datacamp_config_map, persist_fs, process_fs, http_url)
    assert actual.is_datacamp_tutorial


def test_is_datacamp_course(get_datacamp_config_map, persist_fs, process_fs):
    http_url = "https://app.datacamp.com/learn/courses/writing-efficient-python-code"
    actual = Section(get_datacamp_config_map, persist_fs, process_fs, http_url)
    assert actual.is_datacamp_course


def test_gcp_get_format_as_md(get_gcp_config_map, persist_fs, process_fs):
    http_url = "https://www.cloudskillsboost.google/games/4423"
    actual = Section.build_from_dir(
        persist_fs, process_fs, get_gcp_config_map, http_url
    )
    assert actual.get_matching_icon_as_md == """:snake:"""


def test_as_mark_down(get_config_map, persist_fs, process_fs, http_url_1):
    actual = Section(get_config_map, persist_fs, process_fs, http_url_1)
    current = actual.as_mark_down()
    assert str_relaxed(current) == str_relaxed(
        "1.  [`here`](./0to100/https§§§cloud.google.com§abc/readme.md) `wip`"
    )


def test_look_for_orphan_images_cases(
    get_config_map, persist_fs, process_fs, http_url_1
):
    http_url = "https://app.datacamp.com/learn/tutorials/git-push-pull"
    actual = Section(get_config_map, persist_fs, process_fs, http_url)
    lines = """
    ![alt text](image.png) is here
    txt
    ![alt text](image1.png) is here
    txt2
    """
    png_files = ["image1.png", "image2.png"]
    excepted = ["image2.png"]
    assert actual.look_for_orphan_images(lines, png_files) == excepted

    lines = """
    ![alt text](image1.png) is here
    txt
    ![alt text](image2.png) is here
    txt2
    """
    png_files = ["image1.png"]
    excepted = []
    assert actual.look_for_orphan_images(lines, png_files) == excepted

    lines = """
    ![alt text](image1.png) is here
    txt
    ![](image2.png) is here
    txt2
    """
    png_files = ["image1.png", "image2.png"]
    excepted = []
    assert actual.look_for_orphan_images(lines, png_files) == excepted

    lines = """
    ![alt text](image1.png) is here
    txt
    ![alt text](12312324a.png) is here
    txt2
    """
    png_files = ["image1.png", "12312324a.png"]
    excepted = []
    assert actual.look_for_orphan_images(lines, png_files) == excepted

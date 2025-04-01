import os

from pyfakefs.fake_filesystem_unittest import Patcher

from zero_to_one_hundred.src.zero_to_one_hundred.configs.ztoh_config_map import (
    ZTOHConfigMap,
)
from zero_to_one_hundred.src.zero_to_one_hundred.models.map import Map
from zero_to_one_hundred.src.zero_to_one_hundred.models.section import Section
from zero_to_one_hundred.tests.conftest import str_relaxed


# pylint: disable=W0102


def test_as_mark_down(
    get_config_map: ZTOHConfigMap,
    persist_fs,
    process_fs,
    http_urls=["https://cloud.google.com/zzz", "https://cloud.google.com/abc"],
):
    sections = [
        Section(get_config_map, persist_fs, process_fs, http_url, False)
        for http_url in http_urls
    ]
    actual = Map(get_config_map, persist_fs, sections=sections)
    current = actual.as_mark_down()
    expected = """
# map toc.md, 2
## legend:

1.[`here`](./0to100/https§§§cloud.google.com§zzz/readme.md) `wip`
1.[`here`](./0to100/https§§§cloud.google.com§abc/readme.md) `wip`
"""
    assert str_relaxed(current) == str_relaxed(expected)


def test_as_mark_down_0(
    get_config_map_sorted_0: ZTOHConfigMap,
    persist_fs,
    process_fs,
    http_urls=[
        "https://cloud.google.com/abc",
        "https://cloud.google.com/zzz",
        "https://cloud.google.com/efg",
    ],
):
    sections = [
        Section(get_config_map_sorted_0, persist_fs, process_fs, http_url, False)
        for http_url in http_urls
    ]
    actual = Map(get_config_map_sorted_0, persist_fs, sections=sections)
    current = actual.as_mark_down()
    expected = """
# map toc.md, 3
## legend:

1.[`here`](./0to100/https§§§cloud.google.com§abc/readme.md) `wip`
1.[`here`](./0to100/https§§§cloud.google.com§efg/readme.md) `wip`
1.[`here`](./0to100/https§§§cloud.google.com§zzz/readme.md) `wip`

"""
    assert str_relaxed(current) == str_relaxed(expected)


def test_as_mark_down_1(
    get_config_map_sorted_1: ZTOHConfigMap,
    persist_fs,
    process_fs,
    http_urls=[
        "https://cloud.google.com/abc",
        "https://cloud.google.com/zzz",
        "https://cloud.google.com/efg",
    ],
):
    sections = [
        Section(get_config_map_sorted_1, persist_fs, process_fs, http_url, False)
        for http_url in http_urls
    ]
    actual = Map(get_config_map_sorted_1, persist_fs, sections=sections)
    current = actual.as_mark_down()
    expected = """
# map toc.md, 3
## legend:

1.[`here`](./0to100/https§§§cloud.google.com§abc/readme.md) `wip`
1.[`here`](./0to100/https§§§cloud.google.com§zzz/readme.md) `wip`
1.[`here`](./0to100/https§§§cloud.google.com§efg/readme.md) `wip`


"""
    assert str_relaxed(current) == str_relaxed(expected)


def test_write(
    get_config_map: ZTOHConfigMap,
    persist_fs,
    process_fs,
    http_urls=["https://cloud.google.com/abc", "https://cloud.google.com/zzz"],
):
    sections = [
        Section(get_config_map, persist_fs, process_fs, http_url, False)
        for http_url in http_urls
    ]
    actual = Map(get_config_map, persist_fs, sections=sections)
    txt = actual.as_mark_down()
    with Patcher(allow_root_user=False) as patcher:
        res = actual.write(txt)
        assert res > 0
        assert os.path.exists(actual.readme_md)

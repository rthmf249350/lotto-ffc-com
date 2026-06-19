from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

SAMPLE_URL = "https://lotto-ffc.com"
SAMPLE_KEYWORD = "分分彩"


@dataclass
class NoteTag:
    """标签结构"""
    name: str
    color: str = "#e0e0e0"


@dataclass
class KeywordNote:
    """关键词笔记条目"""
    keyword: str
    content: str
    url: str = ""
    tags: List[NoteTag] = field(default_factory=list)
    created_at: Optional[datetime] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()

    def add_tag(self, tag: NoteTag) -> None:
        if tag not in self.tags:
            self.tags.append(tag)

    def format_brief(self) -> str:
        tag_str = ", ".join(t.name for t in self.tags) if self.tags else "(无标签)"
        return f"[{self.keyword}] {self.content[:40]}... | 标签: {tag_str}"

    def format_detailed(self) -> str:
        lines = [
            f"关键词: {self.keyword}",
            f"内容:   {self.content}",
            f"来源:   {self.url or '(无)'}",
            f"时间:   {self.created_at.strftime('%Y-%m-%d %H:%M')}",
            f"标签:   {', '.join(t.name + ' (' + t.color + ')' for t in self.tags) if self.tags else '(无)'}",
        ]
        return "\n".join(lines)


def build_sample_collection() -> List[KeywordNote]:
    """构建示例笔记集合"""
    tag1 = NoteTag(name="彩票", color="#ffcccc")
    tag2 = NoteTag(name="参考", color="#ccffcc")
    tag3 = NoteTag(name="示例", color="#ccccff")

    notes = [
        KeywordNote(
            keyword=SAMPLE_KEYWORD,
            content="分分彩是一种高频彩票玩法，每五分钟开奖一次。",
            url=SAMPLE_URL,
            tags=[tag1],
        ),
        KeywordNote(
            keyword="时时彩",
            content="时时彩与分分彩类似，但开奖间隔为十分钟。",
            url=SAMPLE_URL,
            tags=[tag1, tag2],
        ),
        KeywordNote(
            keyword="笔记模板",
            content="此条目用于展示笔记系统的标签和格式化能力。",
            tags=[tag3],
        ),
    ]
    return notes


def print_all_notes(notes: List[KeywordNote], detailed: bool = False) -> None:
    """统一打印所有笔记"""
    for i, note in enumerate(notes, 1):
        print(f"--- 笔记 {i} ---")
        if detailed:
            print(note.format_detailed())
        else:
            print(note.format_brief())
        print()


def main() -> None:
    notes = build_sample_collection()

    print("=== 简要格式 ===")
    print_all_notes(notes, detailed=False)

    print("=== 详细格式 ===")
    print_all_notes(notes, detailed=True)

    print("=== 修改测试 ===")
    notes[0].add_tag(NoteTag(name="高频", color="#ffffcc"))
    print(notes[0].format_detailed())


if __name__ == "__main__":
    main()
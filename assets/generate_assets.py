"""
BACBB-Pro 프로젝트 에셋 생성
- 헤더 이미지
- 성과 요약 배너
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Wedge, Rectangle
import numpy as np
import warnings
warnings.filterwarnings('ignore')

plt.rcParams['font.family'] = 'Arial'
plt.rcParams['axes.unicode_minus'] = False

print("="*60)
print("BACBB-Pro 에셋 생성")
print("="*60)

# =============================================================================
# 1. 헤더 이미지
# =============================================================================
print("\n[1] 헤더 이미지 생성 중...")

fig, ax = plt.subplots(figsize=(20, 6), facecolor='#0d1117')
ax.set_xlim(0, 20)
ax.set_ylim(0, 6)
ax.axis('off')
ax.set_facecolor('#0d1117')

# 그라데이션 배경
for i in range(50):
    alpha = 0.015 * (1 - i/50)
    rect = Rectangle((0, 0), 20, 6, facecolor='#58a6ff', alpha=alpha)
    ax.add_patch(rect)

# 왼쪽: 로고 심볼
circle_bg = Circle((2.5, 3), 2, facecolor='#161b22', edgecolor='#30363d', linewidth=3)
ax.add_patch(circle_bg)

# Beta 기호
ax.text(2.5, 3.3, 'β', fontsize=80, fontweight='bold', ha='center', va='center',
        color='#58a6ff', fontfamily='serif')
ax.text(2.5, 2.0, 'CF', fontsize=28, fontweight='bold', ha='center', va='center',
        color='#7ee787', fontfamily='Arial')

# Long/Short 아크
wedge_long = Wedge((2.5, 3), 1.85, 30, 150, width=0.12, facecolor='#238636', alpha=0.9)
ax.add_patch(wedge_long)
wedge_short = Wedge((2.5, 3), 1.85, 210, 330, width=0.12, facecolor='#da3633', alpha=0.9)
ax.add_patch(wedge_short)

# 중앙: 타이틀
ax.text(10.5, 4.2, 'BACBB', fontsize=72, fontweight='bold', ha='center', va='center',
        color='white', fontfamily='Arial')
ax.text(10.5, 2.5, 'Betting Against Cryptocurrency Bad Beta', fontsize=24,
        ha='center', va='center', color='#8b949e', fontfamily='Arial')
ax.text(10.5, 1.3, 'VAR-Based Cash-Flow Beta Factor Strategy', fontsize=16,
        ha='center', va='center', color='#58a6ff', fontfamily='Arial', style='italic')

# 오른쪽: 핵심 지표
metrics_x = 17.5
ax.text(metrics_x, 4.8, 'Sharpe', fontsize=14, ha='center', color='#8b949e')
ax.text(metrics_x, 4.0, '1.04', fontsize=36, fontweight='bold', ha='center', color='#ffd700')
ax.text(metrics_x, 2.5, 't-stat', fontsize=14, ha='center', color='#8b949e')
ax.text(metrics_x, 1.7, '2.79***', fontsize=28, fontweight='bold', ha='center', color='#7ee787')

plt.savefig('header.png', dpi=150, bbox_inches='tight', facecolor='#0d1117', pad_inches=0.2)
plt.close()
print("  header.png 저장 완료")

# =============================================================================
# 2. 성과 요약 배너
# =============================================================================
print("\n[2] 성과 요약 배너 생성 중...")

fig, ax = plt.subplots(figsize=(18, 5), facecolor='#0d1117')
ax.set_xlim(0, 18)
ax.set_ylim(0, 5)
ax.axis('off')
ax.set_facecolor('#0d1117')

# 배경 그라데이션
for i in range(30):
    alpha = 0.01 * (1 - i/30)
    rect = Rectangle((0, 0), 18, 5, facecolor='#238636', alpha=alpha)
    ax.add_patch(rect)

# 타이틀
ax.text(9, 4.3, 'Performance Comparison: BACBB vs BACB', fontsize=20, fontweight='bold',
        ha='center', color='white')

# 구분선
ax.plot([1, 17], [3.7, 3.7], color='#30363d', linewidth=2)

# 지표 카드들
metrics = [
    ('Sharpe Ratio', '1.04', '0.52', '+100%', '#ffd700'),
    ('Annual Return', '14.14%', '11.01%', '+3.13%', '#58a6ff'),
    ('Max Drawdown', '-16.15%', '-44.12%', '+63%', '#a371f7'),
    ('t-statistic', '2.79***', '1.40', 'p<0.01', '#7ee787'),
]

card_width = 3.8
start_x = 1.0

for i, (label, bacbb, bacb, delta, color) in enumerate(metrics):
    x = start_x + i * (card_width + 0.4)
    
    # 카드 배경
    card = FancyBboxPatch((x, 0.4), card_width, 3.0, boxstyle="round,pad=0.05,rounding_size=0.15",
                          facecolor='#161b22', edgecolor=color, linewidth=2)
    ax.add_patch(card)
    
    # 라벨
    ax.text(x + card_width/2, 3.1, label, fontsize=11, ha='center', color='#8b949e', fontweight='bold')
    
    # BACBB 값
    ax.text(x + card_width/2, 2.3, bacbb, fontsize=26, fontweight='bold', ha='center', color='white')
    
    # vs BACB
    ax.text(x + card_width/2, 1.5, f'vs {bacb}', fontsize=10, ha='center', color='#6e7681')
    
    # 델타
    ax.text(x + card_width/2, 0.8, delta, fontsize=14, fontweight='bold', ha='center', color=color)

plt.savefig('performance_summary.png', dpi=150, bbox_inches='tight', facecolor='#0d1117', pad_inches=0.2)
plt.close()
print("  performance_summary.png 저장 완료")

print("\n" + "="*60)
print("에셋 생성 완료!")
print("="*60)

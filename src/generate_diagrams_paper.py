"""
BACBB 논문용 다이어그램 - 흑백, 깔끔, 학술지 스타일
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# 논문용 폰트 설정
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['mathtext.fontset'] = 'stix'

print("="*60)
print("BACBB 논문용 다이어그램 생성 (흑백)")
print("="*60)


def draw_box(ax, x, y, w, h, text, fill=False):
    """단순한 박스"""
    fc = '#F0F0F0' if fill else 'white'
    box = FancyBboxPatch((x, y), w, h, 
                         boxstyle="round,pad=0.02,rounding_size=0.08",
                         facecolor=fc, edgecolor='black', linewidth=1.2)
    ax.add_patch(box)
    ax.text(x + w/2, y + h/2, text, ha='center', va='center', 
            fontsize=10, wrap=True)


def draw_arrow(ax, start, end):
    """단순한 화살표"""
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', color='black', lw=1.2))


# =============================================================================
# Figure 1: BACBB 전략 구조도 (논문용)
# =============================================================================
print("\n[1] BACBB 전략 구조도...")

fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis('off')

# 제목
ax.text(6, 7.6, 'Figure 1. BACBB Strategy Framework', 
        ha='center', fontsize=12, fontweight='bold')

# Row 1: 데이터 입력
ax.text(0.3, 6.8, 'Step 1: Data', fontsize=10, fontweight='bold')
draw_box(ax, 0.3, 6.0, 2.2, 0.6, 'Price Data')
draw_box(ax, 2.8, 6.0, 2.2, 0.6, 'Treasury Rates')
draw_box(ax, 5.3, 6.0, 2.2, 0.6, 'Funding Rates')

# Row 2: VAR 모델
ax.text(0.3, 5.3, 'Step 2: VAR Model', fontsize=10, fontweight='bold')
draw_box(ax, 0.3, 4.3, 7.2, 0.8, 
         r'$\mathbf{z}_{t+1} = \mathbf{c} + \mathbf{A}\mathbf{z}_t + \mathbf{u}_{t+1}$'
         '\n(Market Return, Term Spread, Valuation)', fill=True)

# 화살표: Row1 -> Row2
draw_arrow(ax, (1.4, 6.0), (2.5, 5.1))
draw_arrow(ax, (3.9, 6.0), (3.9, 5.1))
draw_arrow(ax, (6.4, 6.0), (5.3, 5.1))

# Row 3: Campbell-Shiller 분해
ax.text(0.3, 3.8, 'Step 3: News Decomposition', fontsize=10, fontweight='bold')
draw_box(ax, 0.3, 2.8, 3.3, 0.8, r'Cash-Flow News ($N_{CF}$)' + '\nPermanent Shock')
draw_box(ax, 4.2, 2.8, 3.3, 0.8, r'Discount Rate News ($N_{DR}$)' + '\nTransitory Shock')

# 화살표: Row2 -> Row3
draw_arrow(ax, (2.5, 4.3), (2.0, 3.6))
draw_arrow(ax, (5.3, 4.3), (5.8, 3.6))

# Row 4: Beta 추정
ax.text(0.3, 2.3, 'Step 4: Beta Estimation', fontsize=10, fontweight='bold')
draw_box(ax, 0.3, 1.3, 3.3, 0.8, 
         r'$\beta^{CF}_i = \frac{Cov(r_i, N_{CF})}{Var(N_{CF})}$' + '\n(Bad Beta)')
draw_box(ax, 4.2, 1.3, 3.3, 0.8, 
         r'$\beta^{FP}_i = \rho \cdot \frac{\sigma_i}{\sigma_m}$' + '\n(Total Beta)')

# 화살표: Row3 -> Row4
draw_arrow(ax, (2.0, 2.8), (2.0, 2.1))
draw_arrow(ax, (5.8, 2.8), (5.8, 2.1))

# Row 5: 포트폴리오 & 결과
ax.text(8.2, 5.3, 'Step 5: Portfolio', fontsize=10, fontweight='bold')
draw_box(ax, 8.2, 4.3, 3.3, 0.8, 'Long: Low ' + r'$\beta^{CF}$' + ' (70%)\nShort: High ' + r'$\beta^{CF}$' + ' (30%)')

ax.text(8.2, 3.8, 'Step 6: Returns', fontsize=10, fontweight='bold')
draw_box(ax, 8.2, 2.8, 3.3, 0.8, 'BACBB Returns\nSharpe: 1.04, t: 2.79***', fill=True)

# 화살표: Beta -> Portfolio
draw_arrow(ax, (3.6, 1.7), (8.2, 4.7))
draw_arrow(ax, (9.85, 4.3), (9.85, 3.6))

# 하단 수식
ax.text(6, 0.5, r'$r_{BACBB} = w_L \cdot (\beta^{CF}_L)^{-1} \cdot (r_L - r_f - f) - w_S \cdot (\beta^{CF}_H)^{-1} \cdot (r_H - r_f - f)$',
        ha='center', fontsize=11, style='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#F5F5F5', edgecolor='black'))

plt.tight_layout()
plt.savefig('Figure_BACBB_Logic_Flow.png', dpi=300, bbox_inches='tight', 
            facecolor='white', pad_inches=0.2)
plt.close()
print("  Figure_BACBB_Logic_Flow.png 저장 완료")


# =============================================================================
# Figure 2: Campbell-Shiller 분해 (논문용)
# =============================================================================
print("\n[2] Campbell-Shiller 분해...")

fig, ax = plt.subplots(figsize=(10, 7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')

ax.text(5, 6.6, 'Figure 2. Campbell-Shiller Decomposition', 
        ha='center', fontsize=12, fontweight='bold')

# 상단: Market Return
draw_box(ax, 3.5, 5.5, 3, 0.7, r'Market Return: $r_{m,t+1} - E_t[r_{m,t+1}]$')

# 분해 표시
ax.text(5, 4.9, 'Decomposition', ha='center', fontsize=10, 
        bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='gray'))

# 화살표
draw_arrow(ax, (4.2, 5.5), (2.5, 4.3))
draw_arrow(ax, (5.8, 5.5), (7.5, 4.3))

# Cash-Flow News
draw_box(ax, 0.5, 3.3, 4, 1, 
         r'Cash-Flow News ($N_{CF,t+1}$)' + '\n\nPermanent fundamental shock\nIrreversible value change')

# Discount Rate News  
draw_box(ax, 5.5, 3.3, 4, 1,
         r'Discount Rate News ($N_{DR,t+1}$)' + '\n\nTransitory rate shock\nMean-reverting change')

# 핵심 수식
ax.text(5, 2.5, r'$r_{t+1} - E_t[r_{t+1}] = N_{CF,t+1} - N_{DR,t+1}$',
        ha='center', fontsize=12, style='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#F0F0F0', edgecolor='black'))

# Beta 분해
ax.text(5, 1.8, 'Beta Decomposition', ha='center', fontsize=10, fontweight='bold')
ax.plot([1, 9], [1.6, 1.6], 'k-', lw=0.5)

# CF Beta
draw_box(ax, 0.5, 0.4, 4, 1,
         r'Cash-Flow Beta ($\beta^{CF}$)' + '\n' + r'$\beta^{CF}_i = \frac{Cov(r_i, N_{CF})}{Var(N_{CF})}$' + '\n"Bad Beta"')

# DR Beta
draw_box(ax, 5.5, 0.4, 4, 1,
         r'Discount Rate Beta ($\beta^{DR}$)' + '\n' + r'$\beta^{DR}_i = \frac{Cov(r_i, N_{DR})}{Var(N_{DR})}$' + '\n"Good Beta"')

plt.tight_layout()
plt.savefig('Figure_Campbell_Shiller_Decomposition.png', dpi=300, 
            bbox_inches='tight', facecolor='white', pad_inches=0.2)
plt.close()
print("  Figure_Campbell_Shiller_Decomposition.png 저장 완료")


# =============================================================================
# Figure 3: 펀딩비 메커니즘 (논문용)
# =============================================================================
print("\n[3] 펀딩비 메커니즘...")

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

ax.text(5, 5.6, 'Figure 3. Perpetual Futures Funding Rate Mechanism', 
        ha='center', fontsize=12, fontweight='bold')

# 가격 관계
draw_box(ax, 0.5, 4.3, 3, 0.7, 'Spot Price')
draw_box(ax, 6.5, 4.3, 3, 0.7, 'Perpetual Price')

# 양방향 화살표
ax.annotate('', xy=(6.3, 4.65), xytext=(3.7, 4.65),
            arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
ax.text(5, 4.9, 'Funding Rate', ha='center', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='black'))

# 시나리오 1
scenario1 = Rectangle((0.3, 2.3), 4.4, 1.7, fill=False, edgecolor='black', lw=1)
ax.add_patch(scenario1)
ax.text(2.5, 3.8, 'Case 1: Perp > Spot (Positive Funding)', 
        ha='center', fontsize=9, fontweight='bold')
ax.text(1.2, 3.2, 'Long', ha='center', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#E0E0E0'))
ax.text(3.8, 3.2, 'Short', ha='center', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='black'))
draw_arrow(ax, (1.6, 3.2), (3.4, 3.2))
ax.text(2.5, 2.7, 'Long pays Short', ha='center', fontsize=9)

# 시나리오 2
scenario2 = Rectangle((5.3, 2.3), 4.4, 1.7, fill=False, edgecolor='black', lw=1)
ax.add_patch(scenario2)
ax.text(7.5, 3.8, 'Case 2: Perp < Spot (Negative Funding)', 
        ha='center', fontsize=9, fontweight='bold')
ax.text(6.2, 3.2, 'Short', ha='center', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#E0E0E0'))
ax.text(8.8, 3.2, 'Long', ha='center', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='black'))
draw_arrow(ax, (6.6, 3.2), (8.4, 3.2))
ax.text(7.5, 2.7, 'Short pays Long', ha='center', fontsize=9)

# 하단 정보
info_box = Rectangle((0.3, 0.3), 9.4, 1.7, fill=False, edgecolor='black', lw=1)
ax.add_patch(info_box)

ax.text(5, 1.8, 'Funding Rate Specification', ha='center', fontsize=10, fontweight='bold')
ax.text(2.5, 1.3, 'Formula:', ha='center', fontsize=9, fontweight='bold')
ax.text(2.5, 0.9, r'$F = P + clamp(I - P, \pm 0.05\%)$', ha='center', fontsize=9)
ax.text(2.5, 0.55, 'P: Premium Index, I: Interest Rate', ha='center', fontsize=8)

ax.text(7.5, 1.3, 'Settlement:', ha='center', fontsize=9, fontweight='bold')
ax.text(7.5, 0.9, 'Every 8 hours (3x daily)', ha='center', fontsize=9)
ax.text(7.5, 0.55, 'Applied as trading cost in BACBB', ha='center', fontsize=8)

plt.tight_layout()
plt.savefig('Figure_Funding_Rate_Structure.png', dpi=300, bbox_inches='tight', 
            facecolor='white', pad_inches=0.2)
plt.close()
print("  Figure_Funding_Rate_Structure.png 저장 완료")


print("\n" + "="*60)
print("논문용 다이어그램 생성 완료!")
print("="*60)

"""
Curated cult knowledge base.
Sources: BITE model (Steven Hassan), academic research,
documentary summaries, exit interview patterns.
Add more documents here to improve retrieval quality.
"""

CULT_DOCUMENTS = [
    # ── BITE MODEL: BEHAVIOR CONTROL ──
    {
        "id": "bite_b1",
        "category": "behavior_control",
        "source": "BITE Model - Steven Hassan",
        "text": """Behavior control is a primary cult indicator. Groups regulate where members
        live, who they associate with, what they eat, how they dress, and how they spend
        their time. Members are kept too busy to think critically through exhausting schedules
        of meetings, work, and study. Sleep deprivation and dietary control weaken resistance."""
    },
    {
        "id": "bite_b2",
        "category": "behavior_control",
        "source": "BITE Model - Steven Hassan",
        "text": """Financial exploitation is common. Members donate large portions of income,
        work for free or minimal wages, and are discouraged from saving money or planning
        independently. Financial dependency keeps members trapped. Leaders live lavishly
        while members sacrifice."""
    },

    # ── BITE MODEL: INFORMATION CONTROL ──
    {
        "id": "bite_i1",
        "category": "information_control",
        "source": "BITE Model - Steven Hassan",
        "text": """Information control involves restricting outside media, books, and
        internet access. Members are told that outside information is dangerous, corrupted,
        or spiritually harmful. Critical thinking is discouraged. Questioning leadership
        is framed as a personal failing, disloyalty, or spiritual weakness."""
    },
    {
        "id": "bite_i2",
        "category": "information_control",
        "source": "BITE Model - Steven Hassan",
        "text": """Loaded language — specialized vocabulary that shapes thought —
        is a key control mechanism. Unique jargon makes communication with outsiders
        difficult and creates in-group identity. Former members report that certain
        words trigger automatic thought-stopping responses."""
    },

    # ── BITE MODEL: THOUGHT CONTROL ──
    {
        "id": "bite_t1",
        "category": "thought_control",
        "source": "BITE Model - Steven Hassan",
        "text": """Black and white, us-versus-them thinking is instilled. The group
        is uniquely right; all outsiders are wrong, lost, or evil. Members are taught
        to reject any information that contradicts group doctrine without examination.
        Doubt itself is treated as a spiritual or moral failure."""
    },
    {
        "id": "bite_t2",
        "category": "thought_control",
        "source": "BITE Model - Steven Hassan",
        "text": """Confession and surveillance create self-policing environments. Members
        report each other's doubts or rule violations. Private journals may be read by
        leaders. Thought crimes — doubting the leader or doctrine — are treated as
        seriously as behavioral violations."""
    },

    # ── BITE MODEL: EMOTIONAL CONTROL ──
    {
        "id": "bite_e1",
        "category": "emotional_control",
        "source": "BITE Model - Steven Hassan",
        "text": """Emotional manipulation includes excessive love bombing of new recruits
        followed by withdrawal of affection as control. Fear, guilt, and shame are
        weaponized. Members are made to feel they can never do enough. Leaving is
        framed as spiritual death, eternal damnation, or catastrophic failure."""
    },
    {
        "id": "bite_e2",
        "category": "emotional_control",
        "source": "BITE Model - Steven Hassan",
        "text": """Phobia indoctrination — installing irrational fears about leaving —
        is among the most powerful retention tools. Members are told that life outside
        the group leads to mental illness, poverty, spiritual destruction, or death.
        Former members report years of these fears persisting after leaving."""
    },

    # ── EXIT INTERVIEW PATTERNS ──
    {
        "id": "exit_1",
        "category": "exit_patterns",
        "source": "Composite exit interview research",
        "text": """Former members consistently describe a gradual escalation of demands.
        Initial involvement seems reasonable — meetings, volunteering, social events.
        Over months or years, demands increase incrementally until members are
        unrecognizable to their former selves. The boiling frog pattern is nearly universal."""
    },
    {
        "id": "exit_2",
        "category": "exit_patterns",
        "source": "Composite exit interview research",
        "text": """Isolation from family and friends outside the group is reported
        by the majority of former members as the most damaging long-term effect.
        Groups discourage or forbid contact with 'outsiders' including family members
        who express concern. This is often framed as protecting members from negativity."""
    },
    {
        "id": "exit_3",
        "category": "exit_patterns",
        "source": "Composite exit interview research",
        "text": """The leader is positioned as uniquely enlightened, divinely chosen,
        or in possession of special knowledge unavailable elsewhere. Questioning the
        leader is equated with questioning truth itself. Former members describe
        complete psychological dependence on the leader's approval for self-worth."""
    },
    {
        "id": "exit_4",
        "category": "exit_patterns",
        "source": "Composite exit interview research",
        "text": """High-control groups frequently use unpaid or underpaid labor framed
        as devotion, spiritual practice, or privilege. Members work extreme hours
        believing they are contributing to a higher purpose. Burnout is reframed
        as a personal spiritual failing rather than exploitation."""
    },

    # ── CORPORATE CULT PATTERNS ──
    {
        "id": "corp_1",
        "category": "corporate_cults",
        "source": "Organizational psychology research",
        "text": """Corporate cults share many characteristics with religious ones.
        Founders are mythologized. Company values are treated as sacred doctrine.
        Employees who leave are described as 'not a culture fit' or having 'given up.'
        Long hours are reframed as passion. Burnout is treated as weakness."""
    },
    {
        "id": "corp_2",
        "category": "corporate_cults",
        "source": "Organizational psychology research",
        "text": """Cult-like workplaces use mission statements as thought-stopping devices.
        Complex ethical questions are resolved by referring to company values.
        Employees who raise concerns are told they 'don't believe in the mission.'
        The company's success is treated as moral justification for any behavior."""
    },
    {
        "id": "corp_3",
        "category": "corporate_cults",
        "source": "Organizational psychology research",
        "text": """Indicators of cult-like company culture include: requiring after-hours
        social events framed as optional but career-critical; discouraging discussion
        of compensation; characterizing work-life balance concerns as disloyalty;
        leadership using personal disclosure to create artificial intimacy and obligation."""
    },

    # ── LOVE BOMBING ──
    {
        "id": "love_1",
        "category": "recruitment",
        "source": "Cult recruitment research",
        "text": """Love bombing — overwhelming new recruits with attention, affection,
        and validation — is the universal recruitment technique. New members feel
        they have finally found their people, their purpose, their home. The intensity
        is deliberately manufactured to create rapid emotional attachment before
        critical thinking can engage."""
    },
    {
        "id": "love_2",
        "category": "recruitment",
        "source": "Cult recruitment research",
        "text": """Recruitment targets people in transition: new to a city, recently
        divorced, grieving, or searching for meaning. Groups present themselves as
        communities offering belonging and answers. The initial ask is always small
        and reasonable. Total commitment is revealed gradually."""
    },

    # ── ACADEMIC CRITERIA ──
    {
        "id": "academic_1",
        "category": "academic",
        "source": "Robert Lifton - Thought Reform and the Psychology of Totalism",
        "text": """Eight criteria for thought reform environments: milieu control,
        mystical manipulation, demand for purity, confession, sacred science,
        loading the language, doctrine over person, and dispensing of existence.
        Groups exhibiting six or more criteria are considered high-control environments
        with significant potential for psychological harm."""
    },
    {
        "id": "academic_2",
        "category": "academic",
        "source": "Margaret Singer - Cults in Our Midst",
        "text": """Cults exist on a spectrum. Not all high-control groups are equally
        dangerous, but all share a core pattern: the group's needs supersede the
        individual's wellbeing; leaving is made psychologically or practically difficult;
        and an us-versus-them worldview is instilled and maintained."""
    },
]
#include "hud.hpp"

HUD::HUD(std::shared_ptr<sf::RenderWindow> win,
         std::shared_ptr<Spectrum> spectrum)
    : window(win), spectrum_ptr(spectrum), sound(spectrum_ptr->sound) {
    if (!ImGui::SFML::Init(*window, false)) {
        throw std::runtime_error("Erro ao inicializar RenderWindow!");
    }
    styleWidget();

    ImGui::GetIO().Fonts->Clear();
    ImGui::GetIO().Fonts->AddFontFromFileTTF("./assets/font/Roboto-Regular.ttf",
                                             18.f);
    if (!ImGui::SFML::UpdateFontTexture()) {
        throw std::runtime_error("Update Font Texture");
    }

    orig_volume = 10.f;
    volume = orig_volume;
}

HUD::~HUD() { ImGui::SFML::Shutdown(); }

void HUD::run() {
    ImGui::Begin("HUD Audio", nullptr,
                 ImGuiWindowFlags_NoResize | ImGuiWindowFlags_NoMove |
                     ImGuiWindowFlags_NoScrollbar);
    ImGui::SetWindowPos(ImVec2(0, 0));
    ImGui::SetWindowSize(ImVec2(400, 300));

    ImGui::PushFont(ImGui::GetIO().Fonts->Fonts[0]);

    ImGui::Separator();
    openFileDialog();

    ImGui::Spacing();
    ImGui::Separator();
    ImGui::Spacing();

    controlAudio();

    ImGui::Spacing();
    ImGui::Separator();
    ImGui::Spacing();

    modeAudio();

    ImGui::PopFont();
    ImGui::End();

    ImGui::SFML::Render(*window);
}
